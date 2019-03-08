from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.additem, name='additem'),
    path('additem/edit/<int:id>/', views.edititem, name='edit'),

]