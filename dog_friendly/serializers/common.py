from rest_framework import serializers 
from ..models import DogFriendly

class DogFriendlySerializer(serializers.ModelSerializer):
    class Meta:
        model = DogFriendly 
        fields = '__all__' 