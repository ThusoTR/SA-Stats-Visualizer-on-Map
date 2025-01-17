"""SA_Stats_Visualizer URL Configuration

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
from django.urls import path, re_path
from main_application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home_page, name = 'index'),
    re_path(r'^South Africa$', views.load_south_african_stats, name = 'South Africa'),
    path('province/<str:name>', views.loaf_provincial_stats, name = 'provincial'),
    re_path(r'^about$', views.about_page, name = 'about'),
]
