# Convert from python object to json for API 
from .models import API_Django
from rest_framework import serializers

class Food_Serializer(serializers.ModelSerializer):
    class Meta: #metadata that describes model
        model = API_Django
        fields = ["id","name","description"]
        

