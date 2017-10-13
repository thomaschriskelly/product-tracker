from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from . import forms

def index(request):
    context = {
        'products': models.Product.objects.all(),
        'product_form': forms.ProductForm(),
    }
    return render(request, 'index.html', context)

def product(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            models.Product.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')

def locations(request, product_id):
    product = models.Product.objects.get(id=product_id)
    context = {
        'product': product,
        'breadcrumbs': models.Breadcrumb.objects.filter(product=product),
    }
    return render(request, 'locations.html', context)
