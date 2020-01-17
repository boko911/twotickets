from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'pizza_name',
            'size',
            'customer_name',
            'email',
            'phone_number'
        ]