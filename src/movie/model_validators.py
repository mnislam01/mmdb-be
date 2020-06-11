from .model_constants import Rating
from django.core.exceptions import ValidationError


def rating_validator(value):
    for choice in Rating.CHOICES:
        if value == choice[0]:
            return value

    raise ValidationError(
                code="rating_out_of_boundary",
                message=f"Rating should be always between 0-5"
            )