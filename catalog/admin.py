from django.contrib import admin
from .models import Category, Product, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'owner', 'is_published')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'inn', 'address',)
    list_filter = ('country',)
    search_fields = ('country', 'address',)
