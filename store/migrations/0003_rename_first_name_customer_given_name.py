# Generated by Django 5.0.4 on 2024-07-04 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_address_zip"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="first_name",
            new_name="given_name",
        ),
    ]
