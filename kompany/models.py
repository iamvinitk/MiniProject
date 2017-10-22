from django.template.defaultfilters import slugify
from django.db import models


# Create your models here.
# Laptops, Mobiles, Cameras, HeadPhones, TVs


class User(models.Model):
    name = models.CharField(max_length=250, null=False)
    password = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=250, null=False)


class ProductTypes(models.Model):
    type = models.CharField(max_length=250, primary_key=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Products(models.Model):
    product_name = models.CharField(max_length=500)
    type = models.ForeignKey(ProductTypes, on_delete=models.CASCADE)
    product_id = models.IntegerField(primary_key=True)
    product_images = models.CharField(max_length=10000)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Laptops(models.Model):
    product_name = models.CharField(max_length=2000, null=False)
    price = models.CharField(max_length=20, default='0')
    slug_name = models.SlugField(unique=True, null=True, max_length=1000)
    type = models.ForeignKey(ProductTypes, on_delete=models.CASCADE, default='NA')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Laptops, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Laptop"
        verbose_name_plural = "Laptops"


class Mobile(models.Model):
    product_name = models.CharField(max_length=2000, null=False)
    box_contains = models.CharField(max_length=5000)
    model_number = models.CharField(max_length=250)
    model_name = models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    ram = models.CharField(max_length=100)
    storage = models.CharField(max_length=250)
    display_size = models.CharField(max_length=250)
    processor = models.CharField(max_length=250)
    primary_camera = models.CharField(max_length=250)
    secondary_camera = models.CharField(max_length=250)
    battery = models.CharField(max_length=250)
    sensors = models.CharField(max_length=1000)
    warranty = models.CharField(max_length=250)
    type = models.ForeignKey(ProductTypes, on_delete=models.CASCADE, blank=True, null=True)
    slug_name = models.SlugField(unique=True, null=True, max_length=2000)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Mobile, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Mobile"
        verbose_name_plural = "Mobiles"


class ProductImages(models.Model):
    product_id = models.CharField(max_length=2000, null=False)
    image_src = models.CharField(max_length=2500, unique=True, null=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "ProductImage"
        verbose_name_plural = "ProductImages"
