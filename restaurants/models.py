from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=300)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    website = models.URLField(blank=True, null=True)
    is_dog_friendly = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.name} - {self.city}"
