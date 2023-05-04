from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied 
from rest_framework import status
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated

from .models import Favourite
from .serializers.common import FavouriteSerializer
from .serializers.populated import PopulatedFavouriteSerializer

class FavouriteListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, _request):
        favourites = Favourite.objects.all()
        serialized_favourites = PopulatedFavouriteSerializer(favourites, many=True)
        return Response(serialized_favourites.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data["owner"] = request.user.id
        favourite_to_add = FavouriteSerializer(data=request.data)
        try: 
            favourite_to_add.is_valid()
            print(favourite_to_add.is_valid())
            favourite_to_add.save()
            return Response(favourite_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        except:
            return Response("Unprocessible Entity", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class FavouriteDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_favourite(self, pk):
        try:
            return Favourite.objects.get(pk=pk)
        except Favourite.DoesNotExist:
            raise NotFound(detail="can not find favourite with that primary key")
        
    def delete(self, request, pk):
        try:
            favourite_to_delete = self.get_favourite(pk=pk)
            if favourite_to_delete.owner != request.user:
                raise PermissionDenied()
            
            favourite_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favourite.DoesNotExist:
            raise NotFound(detail="Favourite not found")
        
