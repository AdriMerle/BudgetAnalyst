from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='Categories'),
    path('transactions/', views.transactions, name='Transactions'),
    path('transactions/new', views.new_transaction, name='NewTransaction'),
    path('transactions/edit/<int:pk>', views.edit_transaction, name='EditTransaction'),
    path('transactions/delete/<int:pk>', views.delete_transaction, name='DeleteTransaction'),
    path('transactions/import', views.import_transactions, name='ImportTransactions'),
    path('categories/delete/<int:pk>', views.delete_category, name='DeleteCategory'),
]