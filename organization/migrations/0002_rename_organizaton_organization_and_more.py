# Generated by Django 4.2.5 on 2023-09-21 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Organizaton',
            new_name='Organization',
        ),
        migrations.RenameModel(
            old_name='OrganizatonAPIKey',
            new_name='OrganizationAPIKey',
        ),
    ]
