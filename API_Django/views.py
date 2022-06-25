# Create all endpoints ; endpoint is an url you can get data from

from django.http import Http404, JsonResponse
from .models import API_Django
from .serializers import Food_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




#Decorator -> function that describes the functionality of another function

@api_view(['GET','POST'])
def food_list(request,format=None):
    #get all food
    #serialize all food
    #return as json 
    if request.method == 'GET':
        food_list = API_Django.objects.all() #all food objects
        serializer = Food_Serializer(food_list, many=True)
        return Response(serializer.data)
        #return JsonResponse({"Food":serializer.data}) #dict convery list of serializer.data to a Food object

    if request.method == 'POST': #Method to add data to database, take an object -> deserialize it and create Food Object
        serializer =  Food_Serializer(data = request.data) #get data from the request
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def food_detail(request,id,format=None):
    
    
    try:
        food = API_Django.objects.get(pk = id)
    except API_Django.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        

    if request.method == 'GET':
        serializer = Food_Serializer(food)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Food_Serializer(food,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) #implied else statement here

    elif request.method == 'DELETE':
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





    







