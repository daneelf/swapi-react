import requests
import time

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


API_URL= "https://swapi.co/api/"
ALL_FILMS = API_URL + "films/"
ALL_CHARACTERS = API_URL + "people/"  
ALL_SPECIES = API_URL + "species/"
SEARCH_FILM = ALL_FILMS + '?search='


@api_view(['GET'])
def get_films(request):
    contex= {}
    if request.method == "GET":
        r = requests.get(ALL_FILMS)
        if r.status_code == 200:
            data = r.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_film(request,film_id):
    context = {}
    species = []
    species_urls = [] 
    species_data = []
    url = ALL_FILMS + film_id
    if request.method == "GET":
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            species = data['species']
            if species:
                species_urls = [x for x in species]
                for species_url in species_urls:
                    get_request = requests.get(species_url)
                    response_data = get_request.json()
                    species_data.append(response_data)
                context['species'] = species_data
            return Response(species_data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_species(request): 
    if request.method == "GET":
        r = requests.get(ALL_SPECIES )
        if r.status_code == 200:
            data = r.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_species_details(request,species_id):
    request_url = ALL_SPECIES + species_id
    context = {}
    characters = []
    characters_urls = []
    characters_data = []
    if request.method == "GET":
        r = requests.get(request_url)
        if r.status_code == 200:
            data = r.json()
            characters = data['people']
            if characters:
                characters_urls = [x for x in characters]
                for character_url in characters_urls:
                    get_request = requests.get(character_url)
                    response_data = get_request.json()
                    characters_data.append(response_data)
                context['characters'] = characters_data
            return Response(characters_data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_characters(request):
    if request.method == "GET":
        r = requests.get(ALL_CHARACTERS)
        if r.status_code == 200:
            data = r.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_character_details(request,character_id):
    url = ALL_CHARACTERS + character_id
    if request.method == "GET":
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
