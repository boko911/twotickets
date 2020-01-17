# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Pizza, Order
from .forms import OrderForm 
from .filters import OrderFilter

def List_pizzas(request):
    context = {'pizza_list' : Pizza.objects.all()}
    return render(request, 'pizzeria/pizza_list.html', context)

def List_orders(request):
    order_list = Order.objects.all()
    order_filter = OrderFilter(request.GET, queryset=order_list)
    return render(request, 'pizzeria/order_list.html', {'filter' : order_filter})

def create_order(request:HttpRequest):
    form = OrderForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')



