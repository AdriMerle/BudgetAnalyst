# Generated by Django 4.2.5 on 2023-10-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_transaction_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='nom',
            field=models.CharField(max_length=30),
        ),
    ]