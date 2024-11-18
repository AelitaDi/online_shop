from django.contrib import admin
from .models import Article


@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'created_at', 'views_count',)
    search_fields = ('heading', 'content',)
