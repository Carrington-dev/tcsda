from django.contrib import admin
from transact.actions import duplicate_event, mark_as_draft, mark_as_paid
from transact.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'email', 'phone', 'first_name', 'last_name',  'tithe', 'offering', 'local_fund', 'local_fund_type', 'status', 'is_paid', )
    actions = [ duplicate_event, mark_as_draft, mark_as_paid]

    ordering = ['-date_ordered']