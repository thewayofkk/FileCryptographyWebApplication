"""Crypter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from TripleDES import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name="home_page"),
    path('DES3/',views.blanktrides,name="DES3"),
    path('DES3En/',views.trides,name="DES3En"),
    path('DES3Dn/',views.tridesDec,name="DES3Dn"),
    path('RSA/',views.blankrsa,name="RSA"),
    path('RSAEn/',views.RSA,name="RSAEn"),
    path('RSADn/',views.RSADec,name="RSADn"),
    path('TWOFISH/',views.blanktwofish,name="TWOFISH"),
    path('TWOFISHEn/',views.TWOFISH,name="TWOFISHEn"),
    path('TWOFISHDn/',views.TWOFISHDec,name="TWOFISHDn"),
    path('AES/',views.blankAES,name="AES"),
    path('AESEn/',views.AES,name="AESEn"),
    path('AESDn/',views.AESDec,name="AESDn"),
    path('aboutus/',views.aboutus,name="aboutus")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)