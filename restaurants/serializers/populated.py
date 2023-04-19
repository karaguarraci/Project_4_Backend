from .common import RestaurantSerializer
from dog_friendly.serializers.common import DogFriendlySerializer

class PopulatedRestaurantSerializer(RestaurantSerializer):
    dog_friendly = DogFriendlySerializer()
