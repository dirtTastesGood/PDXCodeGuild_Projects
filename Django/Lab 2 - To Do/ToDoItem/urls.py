from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='create'),
    path('show/<int:id>', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('mark_complete/<int:id>', views.mark_complete, name='mark_complete'),
]