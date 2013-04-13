from django.http import HttpResponse
from django.shortcuts import render

from random import sample

from bingo.models import BingoItem
from bingo.settings import card_title, card_width, card_height

def build_items_list():
    items = BingoItem.objects.all()
    return sample(list(items), (card_width * card_height))

def index(request):
    context = {
            'bingo_title': card_title,
            'bingo_card_width': (175 * card_width),
            'bingo_items_list': build_items_list()
            }
    return render(request, 'bingo/index.html', context)
