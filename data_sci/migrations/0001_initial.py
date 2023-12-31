# Generated by Django 4.1.13 on 2023-11-06 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Fat_content",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Fat_content_value", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Product_type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Product_type_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Product_visibility",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Product_visibility_value", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Weight_product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Weight_product_value", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Product_id",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Product_id_value",
                    models.CharField(default="none", max_length=255, null=True),
                ),
                (
                    "Product_type_name",
                    models.CharField(default="none", max_length=255, null=True),
                ),
                (
                    "Fat_content_value",
                    models.CharField(default="none", max_length=255, null=True),
                ),
                ("Product_visibility_value", models.IntegerField()),
                ("Weight_product_value", models.IntegerField()),
                ("added_date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "added_by",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
