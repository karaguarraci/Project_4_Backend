from .common import FavouriteSerializer
# from restaurants.serializers.common import RestaurantSerializer
from jwt_auth.serializers.common import UserSerializer

class PopulatedFavouriteSerializer(FavouriteSerializer):
    # restaurant = RestaurantSerializer()
    owner = UserSerializer()