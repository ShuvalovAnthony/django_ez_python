# Generated by Django 4.1.2 on 2022-12-08 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2022, 12, 8, 13, 20, 21, 247638, tzinfo=datetime.timezone.utc)),
        ),
    ]
