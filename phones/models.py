from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=15)
    image = models.CharField(max_length=99)
    realise_date = models.CharField(max_length=20)
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)