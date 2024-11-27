from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Contacts, Product, Category


class ProductListView(ListView):
    model = Product
    paginate_by = 3


class ProductDetail(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price',)
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ContactsListView(ListView):
    model = Contacts

    def post(self, request):
        name = self.request.POST.get("name")
        phone = self.request.POST.get("phone")
        message = self.request.POST.get("message")
        return HttpResponse(f"Спасибо, {name.title()}! Сообщение получено.")
