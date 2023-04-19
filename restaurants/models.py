from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    # dog_friendly = models.ForeignKey('dog_friendly.DogFriendly', related_name='restaurant', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.name} - {self.city}"
