from typing import Dict, List, Optional, Iterator

class Movie:
    def __init__(self, title: str, director: str, year: int, genre: str) -> None:
        self.title: str = title
        self.director: str = director
        self.year: int = year
        self.genre: str = genre

class MovieCollectionIterator:
    def __init__(self, movies: List[Movie]) -> None:
        self._movies = movies
        self._index = 0

    def __iter__(self) -> 'MovieCollectionIterator':
        return self

    def __next__(self) -> Movie:
        if self._index < len(self._movies):
            movie = self._movies[self._index]
            self._index += 1
            return movie
        raise StopIteration

class MovieCollection:
    def __init__(self) -> None:
        self.movies: Dict[str, Movie] = {}
        self.collections: Dict[str, List[str]] = {}

    def add_movie(self, movie: Movie) -> None:
        """Добавление фильма в коллекцию"""
        self.movies[movie.title] = movie

    def remove_movie(self, title: str) -> None:
        """Удаление фильма из коллекции"""
        if title in self.movies:
            del self.movies[title]
            for collection in self.collections.values():
                if title in collection:
                    collection.remove(title)

    def add_to_collection(self, title: str, collection_name: str) -> None:
        """Добавление фильма в коллекцию"""
        if collection_name in self.collections and title in self.movies:
            self.collections[collection_name].append(title)

    def remove_from_collection(self, title: str, collection_name: str) -> None:
        """Удаление фильма из коллекции"""
        if collection_name in self.collections and title in self.collections[collection_name]:
            self.collections[collection_name].remove(title)

    def search_by_title(self, title: str) -> Optional[Movie]:
        """Поиск фильма по названию"""
        return self.movies.get(title)

    def search_by_director(self, director: str) -> List[Movie]:
        """Поиск фильмов по режиссёру"""
        return [movie for movie in self.movies.values() if movie.director == director]

    def search_by_year(self, year: int) -> List[Movie]:
        """Поиск фильмов по году выпуска"""
        return [movie for movie in self.movies.values() if movie.year == year]

    def search_by_genre(self, genre: str) -> List[Movie]:
        """Поиск фильмов по жанру"""
        return [movie for movie in self.movies.values() if movie.genre == genre]

    def __iter__(self) -> Iterator[Movie]:
        """Итератор для перебора всех фильмов"""
        return MovieCollectionIterator(list(self.movies.values()))
