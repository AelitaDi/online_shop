from django.http import HttpResponse
from django.shortcuts import render
from .models import Contacts, Product


def home(request):
    products = Product.objects.order_by('-created_at')[:5]
    for product in products:
        print(product.created_at)
    return render(request, 'home.html')


def contacts(request):
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
