# Generated by Django 3.1.6 on 2021-05-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_auto_20210509_2202"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="birth",
            field=models.DateField(blank=True, null=True),
        ),
    ]