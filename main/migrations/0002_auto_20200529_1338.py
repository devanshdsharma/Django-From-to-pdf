# Generated by Django 3.0.6 on 2020-05-29 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='bpdy',
            new_name='body',
        ),
    ]
