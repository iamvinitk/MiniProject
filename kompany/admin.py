from django.contrib import admin

# Register your models here.
from import_export import resources, fields
from import_export.admin import ImportExportMixin

from kompany.models import Laptops, Mobile, ProductTypes, ProductImages


class LaptopResource(resources.ModelResource):

    class Meta:
        model = Laptops


class LaptopAdmin(ImportExportMixin, admin.ModelAdmin):
    # Fields that we would like to display in Admin Page
    list_filter = ['product_name', ]
    list_display = ('product_name', 'id', )
    resource_class = LaptopResource

    # Auto Field for uniqueness
    prepopulated_fields = {'slug_name': ('product_name',)}


admin.site.register(Laptops, LaptopAdmin)


class MobileResource(resources.ModelResource):
    slug_name = fields.Field(column_name='sl')

    class Meta:
        model = Mobile


class MobileAdmin(ImportExportMixin, admin.ModelAdmin):
    # Fields that we would like to display in Admin Page
    list_filter = ['product_name', 'model_name']
    resource_class = MobileResource
    # Auto Field for uniqueness
    prepopulated_fields = {'slug_name': ('product_name',)}


admin.site.register(Mobile, MobileAdmin)


class ProductImagesAdmin(admin.ModelAdmin):
    # Fields that we would like to display in Admin Page
    list_display = ('product_id', 'image_src')


admin.site.register(ProductImages, ProductImagesAdmin)


class ProductTypeAdmin(admin.ModelAdmin):
    # Fields that we would like to display in Admin Page
    list_display = ('type', )


admin.site.register(ProductTypes, ProductTypeAdmin)
