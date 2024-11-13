from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание товара",
        help_text="Введите описание товара",
    )
    image = models.ImageField(
        upload_to="products/images/",
        blank=True,
        null=True,
        default=None,
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
    )
    price = models.FloatField(
        verbose_name="Стоимость единицы товара",
        help_text="Введите стоимость единицы товара",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price"]


class Contacts(models.Model):
    country = models.CharField(
        max_length=100,
        verbose_name="Страна",
        help_text="Введите название страны",
    )
    inn = models.CharField(
        max_length=50,
        verbose_name="ИНН",
        help_text="Введите ИНН",
    )
    address = models.TextField(
        verbose_name="Адрес",
        help_text="Введите адрес",
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"
        ordering = ["country"]
