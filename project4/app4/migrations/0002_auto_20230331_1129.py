# Generated by Django 3.0 on 2023-03-31 05:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app4', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UesrProfileInfo',
            new_name='UserProfileInfo',
        ),
    ]
