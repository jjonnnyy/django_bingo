from django.contrib import admin
from django_bingo.models import BingoItem

class BingoAdmin(admin.ModelAdmin):
    fields = ('text',)
    list_display = ('text',)

admin.site.register(BingoItem, BingoAdmin)
