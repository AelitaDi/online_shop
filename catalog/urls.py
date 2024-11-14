from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_list, product_info, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products_list/', products_list, name='products_list'),
    path('product_info/<int:pk>/', product_info, name='product_info'),
    path('add_product/', add_product, name='add_product')
]
