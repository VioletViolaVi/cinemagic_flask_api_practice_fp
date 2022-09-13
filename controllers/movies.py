all_cinemagic_movies = [
    {'id': 1, 'movie_name': 'Bitter Sweet'},
    {'id': 2, 'movie_name': 'Death by Rose'},
    {'id': 3, 'movie_name': 'Hollow Winds'},
    {'id': 4, 'movie_name': 'S\'Yan'},
    {'id': 5, 'movie_name': 'Serayah'},
    {'id': 6, 'movie_name': 'Submerged'},
    {'id': 7, 'movie_name': 'Survivalist Returns'},
    {'id': 8, 'movie_name': 'The Lost Galaxy'},
    {'id': 9, 'movie_name': 'Broken'},
    {'id': 10, 'movie_name': 'Roldo'}
]


def index(req):
    return [m for m in cinemagic_movies], 200


# def create(req):
#     new_movie = req.get_json()
