from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Contacts, Product, Category

from .forms import ProductForm, ProductModerForm


class ProductListView(ListView):
    model = Product
    paginate_by = 3


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModerForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("catalog.delete_product") or user == self.object.owner:
            return self.form_class
        raise PermissionDenied

    def form_valid(self, form):
        user = self.request.user
        if user.has_perm("catalog.delete_product") or user == self.object.owner:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        raise PermissionDenied


class ContactsListView(ListView):
    model = Contacts

    def post(self, request):
        name = self.request.POST.get("name")
        phone = self.request.POST.get("phone")
        message = self.request.POST.get("message")
        return HttpResponse(f"Спасибо, {name.title()}! Сообщение получено.")
