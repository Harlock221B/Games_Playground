# Generated by Django 3.2.6 on 2021-08-17 12:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='games',
            name='lancamento',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 12, 22, 44, 974492, tzinfo=utc)),
        ),
    ]