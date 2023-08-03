"""Product URL Configuration

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
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productform/', view.ProductForm),
    path('fetchallproducttype/', view.FetchAllProductType),
    path('fetchallcompanyname/', view.FetchAllCompanyType),
    path('fetchallproductmodel/', view.FetchAllModelType),
    path('productsubmit',view.ProductSubmit),
    path('fetchallrecord/',view.DisplayAllProduct),
    path('displaybyid/',view.DisplayById),
    path('edit_product_data',view.Edit_Product_Data),
    path('displaypicture',view.DisplayPicture),
    path('edit_picture',view.Edit_Picture),
]
