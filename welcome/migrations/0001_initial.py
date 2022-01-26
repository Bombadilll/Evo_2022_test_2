# Generated by Django 4.0.1 on 2022-01-25 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_visitor', models.TextField(max_length=30, unique=True)),
                ('is_welcome', models.BooleanField(default=False)),
                ('date_visit', models.DateTimeField(default=datetime.datetime(2022, 1, 25, 23, 3, 17, 982132))),
            ],
        ),
    ]