from django.db import models
from base.models import BaseModel
from .model_validators import rating_validator
from .model_constants import Rating
from django.contrib.auth import get_user_model

User = get_user_model()


class Genre(BaseModel):

    name = models.CharField(
        max_length=255,
        blank=False
    )
    description = models.TextField(
        blank=True
    )

    @property
    def genre_description(self) -> str:
        """
        Check if the description is available,
        if not return name. 
        """
        des = self.description
        if not des:
            des = self.name
        return des


class Movie(BaseModel):
    genre = models.ManyToManyField(Genre, related_name="movies")
    name = models.CharField(
        max_length=255,
        blank=False
    )
    year = models.IntegerField(
        blank=True
    )
    rating = models.IntegerField(
        choices=Rating.CHOICES,
        default=Rating.zero_star,
        validators=[rating_validator],
        blank=False
    )
    image = models.ImageField(
        blank=True,
        upload_to='images/%Y/%m/%d/'
    )


class WatchList(BaseModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watch_list")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'movie']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['user', 'movie'], name="unique_movie_list")
        ]
