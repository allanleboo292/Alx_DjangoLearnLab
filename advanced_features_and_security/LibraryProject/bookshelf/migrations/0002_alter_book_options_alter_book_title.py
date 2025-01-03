# Generated by Django 5.1.3 on 2024-11-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookshelf", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "permissions": [
                    ("can_view", "Can view book"),
                    ("can_create", "Can create book"),
                    ("can_edit", "Can edit book"),
                    ("can_delete", "Can delete book"),
                ]
            },
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
