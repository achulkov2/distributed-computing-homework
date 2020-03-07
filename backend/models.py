from django.db import models

MAX_LENGTH = 500


class Item(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    code = models.CharField(max_length=MAX_LENGTH)
    category = models.CharField(max_length=MAX_LENGTH)
