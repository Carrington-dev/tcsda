from rest_framework import serializers
from transact.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    order_total       = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    is_paid           = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'email', 'phone', 'first_name', 'last_name',  'tithe', 'offering', 'order_total', 'is_paid', )

    def create(self, validated_data):
        order = super().create(validated_data)
        # order.save()
        return order

    def update(self, instance, validated_data):
        order = super().update(instance, validated_data)
        return order