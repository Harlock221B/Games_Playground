# Generated by Django 3.2.4 on 2021-10-19 11:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20211002_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='lancamento',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 19, 11, 38, 32, 320153, tzinfo=utc)),
        ),
    ]
