from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)
    source = models.CharField(max_length=255)
    sales_assiociate = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='clients_added')
    onboarded_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    payment_type = models.CharField(max_length=100)
    plan = models.Choices('Basic', 'Standard', 'Premium') # To be updated as per actual plans
    activity_status = models.BooleanField(default=True)
    cancelled_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name