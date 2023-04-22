from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'jwt_auth.User', 
        related_name='reviews', 
        on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner.username} - {self.restaurant.name}'

