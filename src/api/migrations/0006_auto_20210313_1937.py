# Generated by Django 3.1.6 on 2021-03-13 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_point_deleted"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={"verbose_name": "город", "verbose_name_plural": "города"},
        ),
        migrations.AlterModelOptions(
            name="client",
            options={"verbose_name": "клиент", "verbose_name_plural": "клиенты"},
        ),
        migrations.AlterModelOptions(
            name="clientfeedback",
            options={
                "verbose_name": "обратная связь",
                "verbose_name_plural": "обратная связь",
            },
        ),
        migrations.AlterModelOptions(
            name="country",
            options={"verbose_name": "страна", "verbose_name_plural": "страны"},
        ),
        migrations.AlterModelOptions(
            name="dispute",
            options={"verbose_name": "спор", "verbose_name_plural": "споры"},
        ),
        migrations.AlterModelOptions(
            name="disputecomment",
            options={
                "verbose_name": "комментарий к спору",
                "verbose_name_plural": "комментарии к спору",
            },
        ),
        migrations.AlterModelOptions(
            name="disputestatus",
            options={
                "verbose_name": "статус спора",
                "verbose_name_plural": "статусы спора",
            },
        ),
        migrations.AlterModelOptions(
            name="executor",
            options={
                "verbose_name": "исполнитель",
                "verbose_name_plural": "исполнители",
            },
        ),
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "заказ", "verbose_name_plural": "заказы"},
        ),
        migrations.AlterModelOptions(
            name="point",
            options={"verbose_name": "точка", "verbose_name_plural": "точки"},
        ),
        migrations.AlterModelOptions(
            name="pointnotification",
            options={"verbose_name": "оповещение", "verbose_name_plural": "оповещения"},
        ),
        migrations.AlterModelOptions(
            name="pointphoto",
            options={
                "verbose_name": "фото для точки",
                "verbose_name_plural": "фото для точки",
            },
        ),
        migrations.AlterModelOptions(
            name="relation",
            options={"verbose_name": "родство", "verbose_name_plural": "родства"},
        ),
        migrations.AlterModelOptions(
            name="service",
            options={"verbose_name": "сервис", "verbose_name_plural": "сервисы"},
        ),
    ]
