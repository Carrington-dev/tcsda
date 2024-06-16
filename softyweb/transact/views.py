from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from transact.models import Order
from transact.serializers import OrderCreateSerializer

class OrderViewSet(ModelViewSet):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()