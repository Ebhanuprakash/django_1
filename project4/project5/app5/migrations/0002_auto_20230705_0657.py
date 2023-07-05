# Generated by Django 3.0 on 2023-07-05 01:27

import django.contrib.auth.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('Email_id', models.EmailField(max_length=254, unique=True, verbose_name=django.contrib.auth.models.User)),
                ('Account_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name=django.contrib.auth.models.User)),
                ('Account_name', models.CharField(max_length=255, verbose_name=django.contrib.auth.models.User)),
                ('Website', models.URLField(blank=True, verbose_name=django.contrib.auth.models.User)),
            ],
        ),
        migrations.DeleteModel(
            name='BooksModel',
        ),
    ]
