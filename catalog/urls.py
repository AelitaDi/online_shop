from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetail, ProductCreateView, ContactsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/list/', ContactsListView.as_view(), name='contacts_list'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create')
]
