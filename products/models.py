from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify
# Create your models here.

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=50)
    logo = models.TextField(default="")
    modified_at = models.DateTimeField(auto_now_add=True)

    # return the object name  in admin page
    def __str__(self):
        return self.name

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=50)
    img = models.TextField(default="")
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Discount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=50)
    desc = models.TextField(default="")
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default="")
    modified_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Country(models.Model):
    country_id = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.country_id

class Product(models.Model):
    GEAR_BOX_CHOICES = [('MT','Manual'),('AT','Automatic')]
    CONDITION_CHOICES = [('new','New'),('old','Old')]
    FUEL_CHOICES = [('gas','Gasoline'), ('diesel','Diesel')]
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=50)
    desc = models.TextField(default="")
    slug = models.SlugField(unique=True,default="", blank=True, null=True)
    brand_id = models.ForeignKey(Brand, verbose_name="Brand", on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, verbose_name="Type", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=11, decimal_places=0)
    car_model = models.IntegerField()
    odo = models.IntegerField()
    country = models.ForeignKey(Country,verbose_name='country', on_delete=models.CASCADE, null=True)
    gear_box = models.CharField(max_length=50, choices=GEAR_BOX_CHOICES, default='')
    condition = models.CharField(max_length=20,choices=CONDITION_CHOICES, default='')
    fuel = models.CharField(max_length=20,choices=FUEL_CHOICES, default='')
    imgs = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-modified_at',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

