# Generated by Django 3.1.7 on 2021-03-08 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_auto_20210308_1753"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="executor",
            name="email",
        ),
    ]
