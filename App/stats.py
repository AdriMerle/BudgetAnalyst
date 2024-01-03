from .models import Transaction, Categorie
import pandas as pd
from django.db.models.functions import TruncDay
from django.db.models import Sum
from .utils import hex_to_rgba

def get_total_par_categorie():
    res = {"entrant" : [], "sortant" : []}
    categories = Categorie.objects.all()
    for categorie in categories :
        transactions = Transaction.objects.filter(categories=categorie)
        total = 0
        for transaction in transactions :
            total += transaction.montant
        if total > 0 :
            res["entrant"].append({"nom" : categorie.nom,
                                   "total" : total,
                                   "couleur" : hex_to_rgba(categorie.couleur)})
        else :
            res["sortant"].append({"nom" : categorie.nom,
                                   "total" : -total,
                                   "couleur" : hex_to_rgba(categorie.couleur)})
    return res

def get_evolution():
    transactions = Transaction.objects.annotate(day=TruncDay('date')).values('day').annotate(total=Sum('montant')).order_by('day')
    evolution = {}
    balance = 0
    for transaction in transactions:
        balance += transaction['total']
        evolution[transaction['day'].strftime("%Y-%m-%d")] = balance
    return evolution