from django.http import HttpResponse
from django.shortcuts import render

from random import sample, shuffle

from django_bingo.models import BingoItem
from django_bingo.settings import card_title, card_width, card_height

def build_items_list():
    items_required = card_width * card_height
    items = list(BingoItem.objects.all())
    if len(items) >= items_required:
        return sample(items, items_required)
    else:
        shuffle(items)
        return items


def index(request):
    context = {
            'bingo_title': card_title,
            'bingo_card_width': (175 * card_width),
            'bingo_items_list': build_items_list()
            }
    return render(request, 'bingo/index.html', context)
