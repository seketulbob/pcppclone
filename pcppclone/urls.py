"""
URL configuration for pcppclone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from main.views import home, processor, graphic_card, motherboards, memories, storages, cases, power_supplies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('processor/', processor, name='processor'),
    path('graphic_card/', graphic_card, name='graphic_card'),
    path('motherboards/', motherboards, name='motherboards'),
    path('memories/', memories, name='memories'),
    path('storages/', storages, name='storages'),
    path('cases/', cases, name='cases'),
    path('power-supplies/', power_supplies, name='power_supplies'),
]
