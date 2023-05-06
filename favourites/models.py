from django.db import models

class Favourite(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, related_name='favourites')
    # reviews = models.ForeignKey('reviews.Review', null=True, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey(
        'jwt_auth.User', 
        related_name='favourites', 
        on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner.username} - {self.restaurant.name}'    