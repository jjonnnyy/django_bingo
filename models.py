from django.db import models

class BingoItem(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text


