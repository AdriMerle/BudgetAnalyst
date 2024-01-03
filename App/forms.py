from django.db import IntegrityError
from django.forms import ModelForm, SelectDateWidget, CheckboxSelectMultiple, TextInput, Form, FileField
from .models import Transaction, Categorie
from crispy_forms.layout import Div
import pandas as pd
import cmapy
import random
from .utils import rgb_to_hex

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'nom', 'montant', 'categories']
        widgets = {
            'date': SelectDateWidget(),
            'categories': CheckboxSelectMultiple(),
        }

class Row(Div):
    css_class = 'row'

class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom', 'couleur']
        widgets = {
            'couleur': TextInput(attrs={'type': 'color', 'name': 'Couleur'}),
        }

class TransactionImportForm(Form):
    file = FileField()

    def process_file(self):
        file = self.cleaned_data['file']
        df = pd.read_csv(file, sep=';')
        df = df.drop(["dateVal", "categoryParent", "comment", "accountNum", "accountLabel", "accountbalance"], axis=1)
        df.rename(columns={"dateOp": "date", "label": "nom", "amount": "montant", "category":"categorie"}, inplace=True)

        try :
            last_date = pd.to_datetime(Transaction.objects.all().order_by('-date').first().date, format='%Y-%m-%d') # get last transaction date
        except(AttributeError):
            last_date = pd.to_datetime("1970-01-01", format='%Y-%m-%d')
        
        df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
        df['montant'] = df['montant'].str.replace(',', '.').astype(float)
        df = df.loc[df['date'] > last_date]

        # Create all the categories that don't already exist
        for categorie in df['categorie'].unique():
            if not Categorie.objects.filter(nom=categorie).exists():
                rgb_color = (random.randrange(0, 256, 10), random.randrange(0, 256, 10), random.randrange(0, 256, 10))
                hex_color = rgb_to_hex(rgb_color)
                Categorie.objects.create(nom=categorie, couleur=hex_color)

        for index, row in df.iterrows():
            try :
                transaction = Transaction.objects.create(date=row['date'], nom=row['nom'], montant=row['montant'])
                transaction.categories.add(Categorie.objects.get(nom=row['categorie']))
                transaction.save()
            except(IntegrityError):
                print(f'{index} : {row["date"]} | {row["nom"]} : {row["montant"]} € ({row["categorie"]}')
