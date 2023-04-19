from .common import DogFriendlySerializer
from restaurants.serializers.common import RestaurantSerializer

class PopulatedDogFriendlySerializer(DogFriendlySerializer):
    restaurant = RestaurantSerializer()