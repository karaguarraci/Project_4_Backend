from .common import RestaurantSerializer
from dog_friendly.serializers.common import DogFriendlySerializer
from reviews.serializers.common import ReviewSerializer
from favourites.serializers.common import FavouriteSerializer

class PopulatedRestaurantSerializer(RestaurantSerializer):
    dog_friendly = DogFriendlySerializer()
    reviews = ReviewSerializer(many=True)
    favourites = FavouriteSerializer(many=True)


