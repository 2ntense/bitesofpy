from dataclasses import dataclass
from dateutil.parser import parse


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    actor_born = parse(actor.born)
    movie_release_date = parse(movie.release_date)
    actor_age_on_movie_release = int((movie_release_date - actor_born).days / 365)

    return f"{actor.name} was {(actor_age_on_movie_release)} years old when {movie.title} came out."
