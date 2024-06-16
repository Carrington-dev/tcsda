import uuid
from django.db import models

from softyweb import settings
from transact.utils import PREFFERED_METHOD, STATUS

    

class Order(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 

    user                    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    email                   = models.EmailField(max_length=200, blank=False)
    first_name              = models.CharField(max_length=200, blank=False)
    last_name               = models.CharField(max_length=200, blank=False)
    phone                   = models.CharField(max_length=50, default="")
    order_total             = models.DecimalField(max_digits=10, decimal_places=2, default=3)
    tithe                   = models.DecimalField(max_digits=10, decimal_places=2, default=3)
    offering                = models.DecimalField(max_digits=10, decimal_places=2, default=3)
    instruction             = models.TextField(default='Gauteng')
    payment_method          = models.CharField(max_length=300, choices=PREFFERED_METHOD, default="PayFast")
    order_number            = models.CharField(max_length=300, blank=False, unique=False, default='')
    device_name             = models.CharField(max_length=700, null=True, blank=True)
    ip_adress               = models.CharField(max_length=40, default="0.0.0.1")
    currency                = models.CharField(max_length=40, default="ZAR")
    country                 = models.CharField(max_length=600,  default='South Africa')
    state                   = models.CharField(max_length=600,  default='Gauteng')
    city                    = models.CharField(max_length=200, blank=True, null=True)
    street_name             = models.CharField(max_length=400, blank=True, null=True)
    zip_code                = models.CharField(max_length=200, blank=True, null=True)
    status                  = models.CharField(max_length=100, choices=STATUS, default="draft")
    date_ordered			= models.DateTimeField(verbose_name='date orderd', auto_now_add=True)
    last_viewed	            = models.DateTimeField(verbose_name='last viewed', auto_now=True)
    is_paid                 = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.order_number}"
    
    def save(self, *args, **kwargs):
        self.order_total =  self.offering + self.tithe
        super(Order, self).save(*args, **kwargs)
    
    def get_order_total(self):
        return self.order_total
    