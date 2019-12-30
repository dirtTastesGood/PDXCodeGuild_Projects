from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='url_shortener_home'),
    path('saveurl/', views.saveurl, name='url_shortener_saveurl'),
    path('redirect/', views.redirect_it, name='url_shortener_redirect_it')
]