from django.shortcuts import get_object_or_404
from django.contrib import messages
from transact.models import Order

def duplicate_event(modeladmin, request, queryset):
        for object in queryset:
            try:
                #obj = Vehicle.objects.get(pk=object.id)
                obj = get_object_or_404(Order, pk=object.id)
                obj.title = str(object.first_name) + f" Copy"
                obj.pk = None
                obj.save()
                messages.success(request, f"{object.first_name} has been dublicated.")
            except:
                pass

duplicate_event.short_description = "Duplicate selected transactions"


def mark_as_draft(self, request, queryset):
    queryset.update(status="draft")
    queryset.update(is_paid=False)
    messages.success(request, f"Marked selected transactions as draft")

mark_as_draft.short_description = "Mark selected transactions as draft"



def mark_as_paid(self, request, queryset):
    queryset.update(status="paid")
    queryset.update(is_paid=True)
    messages.success(request, f"Marked selected transactions as paid")


mark_as_paid.short_description = "Mark selected transactions as paid"