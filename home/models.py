from django.db import models
from products.models import Type,Brand
# Create your models here.
class Spotlight(models.Model):
    name = models.CharField(max_length=60,default='')
    type = models.ForeignKey('products.Type', related_name='spotlight-type+', on_delete=models.CASCADE)
    brand = models.ForeignKey('products.Brand', related_name='spotlight-brand+', on_delete=models.CASCADE)
    link = models.TextField(default='')
    img = models.TextField(default='')
    animation_time = models.FloatField(default=0.0)

    class Meta:
        ordering = ['animation_time']

    def __str__(self):
        return self.brand.name +' '+ self.name+ ' '


