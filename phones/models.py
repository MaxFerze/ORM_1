from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=99)
    realise_date = models.CharField(max_length=20)
    lte_exists = models.BooleanField(max_length=50)
    slug = models.SlugField(max_length=255, verbose_name="URL")