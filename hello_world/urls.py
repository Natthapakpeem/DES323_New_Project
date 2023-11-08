"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hello_world.core import views as core_views
from data_sci import views as data_sci_views

urlpatterns = [
    path("", core_views.index),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("data_sci/", data_sci_views.data_index_view),
    path("data_sci/list_item/all" ,data_sci_views .data_sci_item_list_all ),
    path("data_sci/list_item/id/<id>", data_sci_views.data_sci_item_list_by_id),
    path("data_sci/form/add", data_sci_views.data_sci_item_add),
    path("data_sci/form/edit/<id>", data_sci_views.data_sci_item_edit),
    path("data_sci/form/delete/<id>", data_sci_views.data_sci_item_delete),
    path('import_data_csv/', data_sci_views.import_data_csv),
    path('example_linear_regression', data_sci_views.example_linear_regression),
    path("d3_visualization", core_views.d3_visualization),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


