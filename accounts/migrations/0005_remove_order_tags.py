# Generated by Django 3.0.3 on 2020-06-07 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200607_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
    ]
