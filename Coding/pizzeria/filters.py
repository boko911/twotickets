import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    customer_name = django_filters.CharFilter(method='order_filter')
    class Meta:
        model = Order
        fields = ['customer_name', ]

    def order_filter(self, queryset, name, value):
        return queryset.filter(
            customer_name__icontains=value
        ) | queryset.filter(
            email__icontains=value
        )