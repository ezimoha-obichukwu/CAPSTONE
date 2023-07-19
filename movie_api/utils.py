import requests


# home_page_endpoint = "http://127.0.0.1:8000/"

# # response = requests.get(home_page_endppoint)

# TWO_POST_DATA = {
#     "title":"Blog Post 3",
#     "content":"Blog Post Content",
#     "author":"ina",
#     "source":"channels"
# }
# new_post = requests.post(home_page_endpoint, data=TWO_POST_DATA)
# print(new_post.json())

# endpoint = "https://api.themoviedb.org/3/search/movie?query=Jack+Reacher&api_key=320cb6ed56314c09e3f173b3b8864ef2"

import requests

url = "https://api.themoviedb.org/3/movie/popular"


def get_movie_data(url):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMjBjYjZlZDU2MzE0YzA5ZTNmMTczYjNiODg2NGVmMiIsInN1YiI6IjY0N2Y0MzBiMGUyOWEyMmJlMDhlYWZhNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.u6I_WvuxoOx_bJrsHJXTuVHEoBKU4QdSIL3iP-DW4oc"
    }

    response = requests.get(url, headers=headers)
    movie_dict = response.json()
    return movie_dict

print(get_movie_data(url))

    # print(response.text)
    # response = requests.get(url)
    # movie_dict = dict(response.json())
    # print(movie_dict)
    # print(type(movie_dict))




# my_key = config("MY_TMDB_API_KEY")

# def get_movie_data(url):
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {my_key}"
# }
#     coins = requests.get(url, headers=headers)
#     jsonified = coins.json()
#     return jsonified

# print(get_movie_data(url))

# movie_title = movie_dict
# movie_category = movie_dict
# movie_description = movie_dict
# movie_date_released = movie_dict

# endpoint = "http://127.0.0.1:8000"

# response = requests.post(endpoint, data={"original_title":movie_title, 
# "overview":movie_description, 
# "genre_ids":movie_category, 
# "release_date":movie_date_released})