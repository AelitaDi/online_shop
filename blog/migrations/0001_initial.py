# Generated by Django 5.1.2 on 2024-11-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                (
                    "heading",
                    models.CharField(
                        help_text="Введите заголовок статьи",
                        max_length=250,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="Введите текст статьи",
                        null=True,
                        verbose_name="Содержание",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Загрузите обложку статьи",
                        upload_to="articles/images/",
                        verbose_name="Обложка",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата изменения"),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False, verbose_name="Признак публикации"
                    ),
                ),
                (
                    "views_count",
                    models.IntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
                "ordering": ["heading", "views_count", "created_at"],
            },
        ),
    ]