# Generated by Django 4.0.7 on 2022-09-11 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_medicine_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
