from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name

