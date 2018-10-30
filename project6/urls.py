
from django.contrib import admin
from django.urls import path
import board.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('join', views.join),
    path('login', views.login),
    path('translate', views.translate),
]
