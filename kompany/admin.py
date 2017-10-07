from django.contrib import admin

# Register your models here.
from kompany.models import Laptops


class LaptopAdmin(admin.ModelAdmin):
    # Fields that we would like to display in Admin Page
    list_display = ('product_name', 'processor', 'ram', 'hdd', 'display_size', 'warranty')
    # Auto Field for uniqueness
    prepopulated_fields = {'slug_name': ('product_name',)}


admin.site.register(Laptops, LaptopAdmin)
