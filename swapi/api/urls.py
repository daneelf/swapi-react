"""swapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'films/$',views.get_films,name="get-films"),
    url(r'films/(?P<film_id>[0-9]+)$',views.get_film,name="get-film"),
    url(r'species/$',views.get_species,name="get-species"),
    url(r'species/(?P<species_id>[0-9]+)$',views.get_species_details,name="get-species-details"),
    url(r'characters/$',views.get_characters,name="get-characters"),
    url(r'characters/(?P<character_id>[0-9]+)$',views.get_character_details,name="get-characters-details"),
]

