from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product_type(models.Model):
    Product_type_name = models.CharField(max_length=255)

class Fat_content(models.Model):
    Fat_content_value = models.CharField(max_length=255)

class Product_id(models.Model):
    Product_id_value = models.CharField(max_length=255, default="none", null=True)
    Product_type_name = models.CharField(max_length=255, default="none", null=True)
    Fat_content_value = models.CharField(max_length=255, default="none", null=True)
    Product_visibility_value = models.IntegerField()
    Weight_product_value = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    added_date = models.DateTimeField(default=timezone.now)

class Product_visibility(models.Model):
    Product_visibility_value = models.IntegerField()

class Weight_product(models.Model):
    Weight_product_value = models.IntegerField()



