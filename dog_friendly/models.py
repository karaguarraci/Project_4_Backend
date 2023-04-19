from django.db import models


class DogFriendly(models.Model):
    restaurant = models.OneToOneField('restaurants.Restaurant', related_name='dog_friendly', on_delete=models.CASCADE)
    is_dog_friendly = models.BooleanField(default=False)
    provides_water_bowls = models.BooleanField(default=False)
    has_doggy_menu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.restaurant.name} is dog friendly: {self.is_dog_friendly}"

