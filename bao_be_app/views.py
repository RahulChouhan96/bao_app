from django.shortcuts import render
import requests

# Create your views here.
# myapp/views.py
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.core.cache import cache


def get_people_data(people_api_url):
    response = requests.get(people_api_url)
    response.raise_for_status()
    people_data = response.json()
    return people_data[0]


class ActorData:
    def __init__(self, people_data):
        self.id = people_data["id"]
        self.name = people_data["name"]
        self.species = people_data["species"]
        self.url = people_data["url"]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class SecretKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        secret_key = request.headers.get('Authorization')

        if secret_key == 'ghiblikey':
            # return ('custom_user', None)
            return (User(username = 'custom_user'), None)
        return None


# myapp/views.py

@api_view(['GET'])
@authentication_classes([SecretKeyAuthentication])
@permission_classes([IsAuthenticated])
def get_all_films(request):
    cached_data = cache.get('get_all_films')

    if cached_data:
        print("Returned from cache")
        return Response(cached_data, status=200)
    
    films_api_url = 'https://ghibli.rest/films'

    try:
        response = requests.get(films_api_url)
        response.raise_for_status()
        films_list = response.json()

        film_people_list = []
        for each_film in films_list:
            actors_list = []
            for people_url in each_film["people"]:
                people_data = get_people_data(people_url)
                actor_data = ActorData(people_data).__dict__
                actors_list.append(actor_data)

            each_film["actors"] = actors_list

        return Response(films_list, status=200)

    except requests.RequestException as e:
        # Handle request errors (e.g., connection error, timeout)
        print("ERROR 1", e)
        return Response({'error': str(e)}, status=500)

    except Exception as e:
        # Handle other unexpected errors
        print("ERROR 2", e)
        return Response({'error': str(e)}, status=500)
