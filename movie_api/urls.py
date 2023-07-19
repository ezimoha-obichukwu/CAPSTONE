from django.urls import path
from .views import MovieHomePage, get_external_movies


urlpatterns = [
    path('', MovieHomePage.as_view(), name="home"),
    path('create/', get_external_movies, name='external_api'),
    # path("new/",external_api_movies.as_view(), name="new")
]

