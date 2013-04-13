from django.http import HttpResponse
from django.shortcuts import render

from random import sample

from bingo.models import BingoItem

def build_items_list():
    items = BingoItem.objects.all()
    return sample(list(items), 25)

def index(request):
    context = {'bingo_items_list': build_items_list()}
    return render(request, 'bingo/index.html', context)
