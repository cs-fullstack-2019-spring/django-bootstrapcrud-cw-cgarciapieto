from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ItemModel(models.Model):
    picture=models.CharField(max_length=200)
    URL = models.URLField(max_length=200)
    name =models.CharField(max_length=200)
    description =models.TextField(max_length=1000)
    price = models.IntegerField(default=0)
    item_model = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name