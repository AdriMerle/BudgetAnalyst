# Generated by Django 4.2.5 on 2023-10-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_categorie_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='bg_color',
            field=models.CharField(default='#343a40', max_length=15),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='nom',
            field=models.CharField(max_length=50),
        ),
    ]
