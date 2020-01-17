from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.List_pizzas),
    url(r'^orders/', views.List_orders, name='list_orders'),
    url(r'^create_order/', views.create_order , name= 'create_order')
]