from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('delivery', 'DeliveryMan'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
        ('complete', 'Complete'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    delivery_man = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_orders', limit_choices_to={'role': 'delivery'})
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    payment_status = models.CharField(max_length=10, choices=[('unpaid', 'Unpaid'), ('paid', 'Paid')], default='unpaid')
    stripe_payment_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

