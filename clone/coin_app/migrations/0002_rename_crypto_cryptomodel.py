# Generated by Django 4.1 on 2022-09-04 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coin_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crypto',
            new_name='CryptoModel',
        ),
    ]