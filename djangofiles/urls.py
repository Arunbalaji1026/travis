"""djangofiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.views import APIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('travistest.urls')),
    path('',include('django.contrib.auth.urls')),
]

    #url(r'^admin/',admin.site.urls),
    #url(r'^user/',views.indexList.as_view()),
    # url(r'^employee/',views.selectDetails.as_view()),
    # url(r'^employee/',views.addDetails.as_view()),
    # url(r'^employee/',views.updateDetails.as_view()),
    # url(r'^employee/',views.deleteDetails.as_view()),
