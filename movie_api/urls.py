from django.urls import path
from .views import MovieHomePage


urlpatterns = [
    path('', MovieHomePage.as_view(), name="home"),
    # path("new/",external_api_movies.as_view(), name="new")
]