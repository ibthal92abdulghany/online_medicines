# Generated by Django 4.0.7 on 2022-09-15 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0008_alter_order_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(to='medicine.cart'),
        ),
    ]