from django.db import models
from django.core.exceptions import ValidationError

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    # county = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=300)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    website = models.URLField(blank=True, null=True)
    is_dog_friendly = models.BooleanField(blank=False, default=None)

    def clean(self):
        if self.is_dog_friendly is not True:
            raise ValidationError('Restaurant must be dog friendly.')
   
    
    
    def __str__(self):
        return f"{self.name} - {self.city}"
