from django.db import models

# Create your models here.
class GuestResponse(models.Model):
    guest_name = models.CharField(max_length=100)
    able_to_attend = models.BooleanField()
    adults = models.TextField(blank=True)
    children = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    
    def __str__(self):
        return self.guest_name