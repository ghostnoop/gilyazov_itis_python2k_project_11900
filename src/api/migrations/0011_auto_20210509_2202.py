# Generated by Django 3.1.6 on 2021-05-09 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_auto_20210509_1742"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="religion",
            field=models.CharField(max_length=50, null=True),
        ),
    ]