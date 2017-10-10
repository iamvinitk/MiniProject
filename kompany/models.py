from django.template.defaultfilters import slugify
from django.db import models
# Create your models here.
# Laptops, Mobiles, Cameras, HeadPhones, TVs


class User(models.Model):
    name = models.CharField(max_length=250, null=False)
    password = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=250, null=False)


class Laptops(models.Model):
    product_name = models.CharField(max_length=2000, null=False)
    processor = models.CharField(max_length=2000)
    ram = models.CharField(max_length=100)
    hdd = models.CharField(max_length=250)
    display_size = models.CharField(max_length=250)
    warranty = models.CharField(max_length=1000)
    slug_name = models.SlugField(unique=True)
    image_src = models.URLField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Laptops, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Laptop"
        verbose_name_plural = "Laptops"
