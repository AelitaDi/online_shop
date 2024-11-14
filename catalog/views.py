from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Contacts, Product, Category
from django.core.paginator import Paginator
from .forms import ProductForm


def products_list(request):
    """
    Контроллер обрабатывает GET-запрос, выводит страницу с каталогом товаров.
    """
    products = Product.objects.all()
    p = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, 'products_list.html', context=context)


def home(request):
    """
    Контроллер обрабатывает GET-запрос, выводит домашнюю страницу.
    """
    products = Product.objects.order_by('-created_at')[:3]
    context = {"products": products}
    for product in products:
        print(product.created_at)
    return render(request, 'home.html', context=context)


def contacts(request):
    """
    Контроллер обрабатывает GET- и POST-запросы, выводит страницу с контактными данными.
    """
    contact = Contacts.objects.get(id=1)
    context = {
        'country': contact.country,
        'inn': contact.inn,
        'address': contact.address
    }
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name.title()}! Сообщение получено.")
    return render(request, 'contacts.html', context=context)


def product_info(request, pk):
    """
    Контроллер обрабатывает GET-запрос, выводит страницу с информацией о товаре.
    """
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_info.html', context=context)


def add_product(request):
    """
    Контроллер обрабатывает POST-запрос на добавление нового товара.
    """
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_at = timezone.now()
            product.updated_at = timezone.now()
            product.save()
            return render(request, 'product_info.html', {"product": product})
    else:
        form = ProductForm()
        return render(request, 'new_product.html', {'form': form})
