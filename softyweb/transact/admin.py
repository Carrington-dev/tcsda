from django.contrib import admin
from transact.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'id', 'email', 'phone', 'first_name', 'last_name',  'tithe', 'offering', 'status', )