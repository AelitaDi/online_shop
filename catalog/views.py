from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Contacts, Product, Category
from django.core.paginator import Paginator


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
        name = request.POST.get("name")
        description = request.POST.get("description")
        category_obj = request.POST.get("category")
        categories = Category.objects.all()
        for category in categories:
            if str(category_obj) == str(category.id):
                target_category = category
            else:
                return HttpResponse(f"Выбранная категория не существует.")
        price = request.POST.get("price")
        image = request.POST.get("image")
        product = Product.objects.create(name=name, description=description, price=price, category=target_category,
                                         image=image)
        product.save()
        return HttpResponse(f"Спасибо, товар добавлен в каталог.")
    return render(request, 'add_product.html')
