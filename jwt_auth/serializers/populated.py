from .common import UserSerializer
from favourites.serializers.common import FavouriteSerializer

class PopulatedUserSerializer(UserSerializer):
    favourites = FavouriteSerializer(many=True)