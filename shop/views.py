from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Item, Purchase


def list_item(request):
    item_list = Item.objects.all()
    context = {
        'items': item_list
    }
    return render(request, 'list_item.html', context)


def detail_item(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'detail_item.html', {
        'items': item
    })
