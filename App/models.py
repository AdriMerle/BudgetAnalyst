from django.db import models

# Data models.

class Categorie(models.Model):
    nom = models.CharField(max_length=30, unique=True, blank=False, null=False)
    couleur = models.CharField(max_length=15, blank=False, null=False, default="#343a40")

    def __str__(self):
        return self.nom

class Transaction(models.Model):
    date = models.DateField(blank=False, null=False)
    nom = models.CharField(max_length=50, blank=False, null=False)
    montant = models.FloatField(blank=False, null=False)
    categories = models.ManyToManyField(Categorie, related_name='Transaction', blank=False)

    class Meta:
        unique_together = ('date', 'nom', 'montant')

    def __str__(self):
        return f"{self.date} | {self.nom} : {self.montant} € ({self.categories.all()})"