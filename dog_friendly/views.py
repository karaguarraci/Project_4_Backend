from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound 
from rest_framework import status
from django.db import IntegrityError

from .models import DogFriendly
from .serializers.common import DogFriendlySerializer
from .serializers.populated import PopulatedDogFriendlySerializer

class DogFriendlyListView(APIView):
    
    def get(self, _request):
        dog_friendly_info = DogFriendly.objects.all()
        serialized_dog_friendly_info = PopulatedDogFriendlySerializer(dog_friendly_info, many=True)
        return Response(serialized_dog_friendly_info.data, status=status.HTTP_200_OK)

    def post(self, request):
        dog_friendly_info_to_add = DogFriendlySerializer(data=request.data)
        try:
            dog_friendly_info_to_add.is_valid()
            dog_friendly_info_to_add.save()
            return Response(dog_friendly_info_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessible Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class DogFriendlyDetailView(APIView):
        
        def get_dog_friendly_info(self, pk):
            try:
                return DogFriendly.objects.get(pk=pk)
            except DogFriendly.DoesNotExist:
                raise NotFound(detail="can not find a restaurant with that primary key")
            
        def get(self, _request, pk):
            dog_friendly_info = self.get_dog_friendly_info(pk=pk)
            serialized_single_dog_friendly_info = PopulatedDogFriendlySerializer(dog_friendly_info)
            return Response(serialized_single_dog_friendly_info.data, status=status.HTTP_200_OK)
        
        def put(self, request, pk):
            dog_friendly_info_to_edit = self.get_dog_friendly_info(pk=pk)
            updated_dog_friendly_info = DogFriendlySerializer(dog_friendly_info_to_edit, data=request.data)
            try:
                updated_dog_friendly_info.is_valid()
                updated_dog_friendly_info.save()
                return Response(updated_dog_friendly_info.data, status=status.HTTP_202_ACCEPTED)
            except AssertionError as e:
                return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            except:
                return Response({"detail": "Unprocessible Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
        def delete(self, _request, pk):
            dog_friendly_info_to_delete = self.get_dog_friendly_info(pk=pk)
            dog_friendly_info_to_delete.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)