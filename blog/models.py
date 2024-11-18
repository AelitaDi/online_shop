from django.db import models


class Article(models.Model):
    heading = models.CharField(
        max_length=250,
        verbose_name="Заголовок",
        help_text="Введите заголовок статьи",
    )
    content = models.TextField(
        null=True,
        verbose_name="Содержание",
        help_text="Введите текст статьи",
    )
    image = models.ImageField(
        upload_to="articles/images/",
        verbose_name="Обложка",
        help_text="Загрузите обложку статьи",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    is_published = models.BooleanField(
        default=False, null=False, verbose_name="Признак публикации"
    )

    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.heading

    def views_count_ink(self):
        self.views_count += 1

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["heading", "views_count", "created_at"]
