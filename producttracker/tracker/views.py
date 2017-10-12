from django.shortcuts import render
from . import models

def index(request):
    context = {
        'products': models.Product.objects.all(),
        'breadcrumbs': models.Breadcrumb.objects.all(),
    }
    return render(request, 'index.html', context)

