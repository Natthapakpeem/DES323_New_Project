from django.contrib import admin

from .models import *

@admin.register(Product_id)
class Product_id(admin.ModelAdmin):
    pass

@admin.register(Product_type)
class Product_type(admin.ModelAdmin):
    pass

@admin.register(Fat_content)
class Fat_content(admin.ModelAdmin):
    pass

@admin.register(Product_visibility)
class Product_visibility(admin.ModelAdmin):
    pass

@admin.register(Weight_product)
class Weight_product(admin.ModelAdmin):
    pass

