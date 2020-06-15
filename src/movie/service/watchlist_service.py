from movie.models import WatchList
from base.services import model_service


class WatchListService(model_service.BaseModelService):
    model = WatchList
