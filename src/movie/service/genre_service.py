from movie.models import Genre
from base.services import model_service


class GenreService(model_service.BaseModelService):
    model = Genre
