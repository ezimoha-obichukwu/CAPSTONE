from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework import generics
from .models import Movie
from django.contrib.auth.models import User
from .serializers import Movieserializer
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
import requests
from .utils import get_movie_data
from django.http import HttpResponse



# Create your views here.
class MovieHomePage(ListAPIView):
    queryset = Movie.objects.order_by('-date_released')
    serializer_class = Movieserializer
    permission_classes = [IsAdminUser]
    pagination_class = PageNumberPagination
    page_size = 5
    filter_backends = [SearchFilter]
    search_fields = ["title", "category", "date_released", "category"]

def get_external_movies(request):
    url = "https://api.themoviedb.org/3/movie/popular"

    movies = get_movie_data(url)

    for i in range(11):
        movie_title = movies["results"][i]["title"]
        movie_date_released = movies["results"][i]["release_date"]
        movie_description = movies["results"][i]["overview"]
        movie_ratings = int(movies["results"][i]["vote_average"])
        movie_poster = movies["results"][i]["poster_path"]

        if movie_ratings > 5:
            movie_ratings = 5
        
        Movie.objects.create(title=movie_title, date_released=movie_date_released, rating=movie_ratings, 
                             description=movie_description, poster=movie_poster)

        print(movie_title, movie_date_released, movie_ratings, movie_description)
    return HttpResponse("Movies have been added")
    # url = "https://api.themoviedb.org/3/person/popular?language=en-US&page=1"

    # headers = {
    #     "accept": "application/json",
    #     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMjBjYjZlZDU2MzE0YzA5ZTNmMTczYjNiODg2NGVmMiIsInN1YiI6IjY0N2Y0MzBiMGUyOWEyMmJlMDhlYWZhNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.u6I_WvuxoOx_bJrsHJXTuVHEoBKU4QdSIL3iP-DW4oc"
    # }
    
    # response = requests.get(url, headers=headers)

    # print(response.json())




































# def get_queryset(self):  # Replace with the actual URL of the external API

#     url = "https://api.themoviedb.org/3/person/popular?language=en-US&page=1"

#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMjBjYjZlZDU2MzE0YzA5ZTNmMTczYjNiODg2NGVmMiIsInN1YiI6IjY0N2Y0MzBiMGUyOWEyMmJlMDhlYWZhNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.u6I_WvuxoOx_bJrsHJXTuVHEoBKU4QdSIL3iP-DW4oc"
#     }

#     response = requests.get(url, headers=headers)

#     print(response.json())


#     movies_data = response.json().get('results', [])

#     movies = []
#     movie2 = len(movies_data)
#     for i in range(0, movie2):
#         movie = Movie(
#             title=movies_data[i]['title'],
#             description=movies_data[i]['overview'],
#             date_released=movies_data[i]['released_date']
#         )
#             # actors=movie_data['actors'],
#              # category=movie_data['genre_ids'],
#             # date_released=movie_data['release_date'],
#         # )
#         movies.append(movie)

#     Movie.objects.bulk_create(movies)

#     return HttpResponse("Hello WOrld")

    

#     # def get_queryset(self):
#         # response = requests.get('https://api.themoviedb.org/3/search/movie?query=Jack+Reacher&api_key=320cb6ed56314c09e3f173b3b8864ef2')  # Replace with the actual URL of the external API
#         # movies_data = response.json()

#         # movies = []
#         # for movie_data in movies_data:
#             # movie = Movie(
#                 # title=movie_data['original_title'],
#                 # actors=movie_data['actors'],
#                 # category=movie_data['genre_ids'],
#                 # date_released=movie_data['release_date'],
#             # )
#             # movies.append(movie)

#         # Movie.objects.bulk_create(movies)

#         # return Movie.objects.all()    


