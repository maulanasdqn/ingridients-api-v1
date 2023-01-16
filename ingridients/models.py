from django.utils.timezone import now
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class Ingridients(models.Model):
    name = models.CharField(max_length=120)
    qty = models.IntegerField()
    weight = models.FloatField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

