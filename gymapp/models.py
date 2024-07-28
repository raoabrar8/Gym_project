from datetime import timedelta
from django.db import models
from django.utils import timezone
# Create your models here.


class MemberModel(models.Model):
    
    
    STATUS_CHOICES  = [
        ('Active', 'Active'),
        ('Non Active', 'Non Active'),
    ]
    
    STATUS_FEE = [
        ('Due', 'Due'),
        ('Paid', 'Paid')
    ]
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length = 100)
    fee_amount = models.DecimalField(max_digits=6, decimal_places=2) 
    fee_date = models.DateField()
    picture = models.ImageField(upload_to='memeber_pictures/', blank=True, null=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    fee_status = models.CharField(max_length=10, default='Paid', choices=STATUS_FEE)
    
    
    def __str__(self):
        return self.name
    
    
    def is_date(self):
        return (timezone.now().date() - self.fee_date).days >=28
    
    
    def save(self, *args, **kwargs):
        if self.fee_date < timezone.now().date() - timedelta(days=28):
            self.fee_status = 'Due'
        super().save(*args, **kwargs)
    
    
    