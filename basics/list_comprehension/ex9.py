def get_high_rated_movies(movies):
    return [
        movie['title']
        for movie in movies
        if movie['rating'] is not None and movie['rating'] >= 8
    ]

movies = [
    {"title": "Interstellar", "rating": 8.7},
    {"title": "Arrival", "rating": None},
    {"title": "The Matrix", "rating": 8.7},
    {"title": "Tenet", "rating": 7.3},
    {"title": "Blade Runner 2049", "rating": None},
    {"title": "Dune", "rating": 8.0},
]

result = get_high_rated_movies(movies)

for i in result:
    print(i)