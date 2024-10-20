from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpRequest

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sorty = request.GET.get('sort')
    if sorty == 'name':
        sort_phone = phones.order_by('name')
    elif sorty == 'min_price':
        sort_phone = phones.order_by('price')
    elif sorty == 'max_price':
        sort_phone = phones.order_by('-price')
    else:
        sort_phone = phones
    context = {
        'phones': sort_phone,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.get(slug=str.lower(slug))
    context = {
        'phone': product
    }
    return render(request, template, context)
