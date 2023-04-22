from .common import RestaurantSerializer
from dog_friendly.serializers.common import DogFriendlySerializer
from reviews.serializers.common import ReviewSerializer

class PopulatedRestaurantSerializer(RestaurantSerializer):
    dog_friendly = DogFriendlySerializer()
    reviews = ReviewSerializer(many=True)

