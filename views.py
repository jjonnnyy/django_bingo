from django.http import HttpResponse
from django.shortcuts import render

from bingo.models import BingoItem

def build_items_list():
    return BingoItem.objects.all()


def index(request):
    context = {'bingo_items_list': build_items_list()}
    return render(request, 'bingo/index.html', context)
