# Generated by Django 4.0.7 on 2022-09-14 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newss', '0002_alter_news_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
