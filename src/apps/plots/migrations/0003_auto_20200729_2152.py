# Generated by Django 3.0.3 on 2020-07-29 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0002_auto_20200720_2119'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Datum',
            new_name='DataPoint',
        ),
    ]
