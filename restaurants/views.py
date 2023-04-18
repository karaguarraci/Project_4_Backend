from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound 

from .models import Restaurant
from .serializers.common import RestaurantSerializer

class RestaurantListView(APIView):

    def get(self, _request):
        restaurants = Restaurant.objects.all()
        serialized_restaurants = RestaurantSerializer(restaurants, many=True)
        return Response(serialized_restaurants.data, status=status.HTTP_200_OK)

    def post(self, request):
        restaurant_to_add = RestaurantSerializer(data=request.data)
        try:
            restaurant_to_add.is_valid()
            restaurant_to_add.save()
            return Response(restaurant_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY) 
        
class RestaurantDetailView(APIView):

    def get_restaurant(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise NotFound(detail="can not find a restaurant with that primary key")
        
    def get(self, _request, pk):
        restaurant = self.get_restaurant(pk=pk)
        serialized_single_restaurant = RestaurantSerializer(restaurant)
        return Response(serialized_single_restaurant.data, status=status.HTTP_200_OK)