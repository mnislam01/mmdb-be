from movie.models import Movie
from base.services import model_service


class MovieService(model_service.BaseModelService):
    model = Movie
