from flask import Flask, request, render_template
from flask_cors import CORS
from flask import jsonify
# from dragon import name_generator

# from controllers import cinemagic_movies

server = Flask(__name__)
CORS(server)


@server.route('/')
def home():
    return 'Hello from Flask!'


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


@server.route('/api/movies', methods=["GET", 'POST'])
def movies():
    if request.method == "GET":
        return jsonify({'cinemagic_movies': all_cinemagic_movies})

    if request.method == "POST":
        new_movie_data = request.get_json()
        all_cinemagic_movies.append(new_movie_data)
        new_movie_data.id = len(all_cinemagic_movies)
        return jsonify({"added_movie": new_movie_data})


@server.route('/api/movies/<int:movie_id>')
def single_movie(movie_id):
    movie = all_cinemagic_movies[movie_id-1]
    return jsonify(movie)


# @server.route('/name_generator')
# def get_name():
#     dragon_name = name_generator(request.args)
#     return render_template('result.html', title=f'Hello {dragon_name}!', result=dragon_name)


server.run(debug=True)
