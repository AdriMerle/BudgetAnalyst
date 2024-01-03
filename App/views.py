from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction, Categorie
from .forms import *
from .stats import *

# Create your views here.

def home(request):
    total_par_categorie = get_total_par_categorie()
    context = {
        "entrant_par_categorie" : total_par_categorie["entrant"],
        "sortant_par_categorie" : total_par_categorie["sortant"],
        "evolution" : get_evolution(),
    }
    # print(context)
    return render(request, 'home.html', context)

def categories(request):
    context = {'categories': Categorie.objects.all()}
    if request.method == 'POST':
        context['form'] = CategorieForm(request.POST)
        if context['form'].is_valid():
            categorie = context['form'].save()
            context["categorie"] = categorie
            context["sucess"] = True
        else :
            context["sucess"] = False
    else:
        context['form'] = CategorieForm()

    return render(request,
            'categories.html',
            context)

def delete_category(request, pk):
    category = get_object_or_404(Categorie, pk=pk)
    category.delete()
    request.method = 'GET'
    return redirect('Categories')

def transactions(request):
    return render(request, 'transaction-list.html', {'transactions': Transaction.objects.all()})

def new_transaction(request):
    context = {}
    if request.method == 'POST':
        context['form'] = TransactionForm(request.POST)
        if context['form'].is_valid():
            transaction = context['form'].save()
            context["transaction"] = transaction
            context["sucess"] = True
        else :
            context["sucess"] = False
    else:
        context['form'] = TransactionForm()

    return render(request,
            'transaction-new.html',
            context)


def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('Transactions')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transaction-edit.html', {'form': form})

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    request.method = 'GET'
    return redirect('Transactions')


def import_transactions(request):
    if request.method == 'POST':
        form = TransactionImportForm(request.POST, request.FILES)
        if form.is_valid():
            form.process_file()
    else:
        form = TransactionImportForm()
    return render(request, 'transaction-import.html', {'form': form})