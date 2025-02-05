from typing import List, Dict, Union

# Dictionary of movies

MOVIES = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]


def is_movie_55(name: str) -> bool:
    movie_match = [movie for movie in MOVIES if movie["name"] == name]
    assert movie_match, "no such movie!"
    return movie_match[0]["imdb"] > 5.5


def get_good_movies() -> List[Dict[str, Union[str, float]]]:
    movie_match = [movie for movie in MOVIES if movie["imdb"] > 5.5]
    return movie_match


def get_movies_by_cat(cat_name: str) -> List[Dict[str, Union[str, float]]]:
    movie_match = [movie for movie in MOVIES if movie["category"] == cat_name]
    assert movie_match, "no such category!"
    return movie_match


def get_avg_films_score(candidates: List[str]) -> float:
    scores_sum = 0
    scores_cnt = 0
    for candidate in candidates:
        movie_match = [movie for movie in MOVIES if movie["name"] == candidate]
        assert movie_match, f"no such movie! {candidate}"
        scores_sum += movie_match[0]["imdb"]
        scores_cnt += 1
    return scores_sum / scores_cnt


def get_avg_cat_score(category: str) -> float:
    movie_match = [movie for movie in MOVIES if movie["category"] == category]
    assert movie_match, "no such category"

    return sum([mov["imdb"] for mov in movie_match]) / len(movie_match)
