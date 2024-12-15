# Generated by Django 5.1.3 on 2024-12-15 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="posts", to="blog.tag"
            ),
        ),
    ]
