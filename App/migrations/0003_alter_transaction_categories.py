# Generated by Django 4.2.5 on 2023-10-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_categorie_transaction_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='categories',
            field=models.ManyToManyField(related_name='Transaction', to='App.categorie'),
        ),
    ]
