from .common import FavouriteSerializer
from restaurants.serializers.common import RestaurantSerializer
from jwt_auth.serializers.common import UserSerializer
from reviews.serializers.common import ReviewSerializer


class PopulatedFavouriteSerializer(FavouriteSerializer):
    restaurant = RestaurantSerializer()
    owner = UserSerializer()
    reviews = ReviewSerializer(many=True)