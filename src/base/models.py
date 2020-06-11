import uuid
from django.db import models


class BaseManager(models.Manager):
    """
    The base model manager to be used accross the system
    Either a model have this by default or to customize it 
    should inherit this manager. This could look redundancy
    if not modified but that is something we have to accept 
    to design the software with SOLID principles. Well there are
    always anti patterns, aren't there?
    I think we can do some optimization here and use this manager as default
    """
    pass


class BaseModel(models.Model):
    """
    Base model to be inherited by every model
    fields of this model is common to all model across the system
    changes in the model should not be directed to one particular model
    or should not bread or modify a single model state. Changes should reflect
    across all the models.

    For field level validation it is advised to user clean_field() method
    """
    uuid = models.UUIDField(
        default = uuid.uuid4,
        editable = False,
        help_text="Unique identifer accross different system. this is guaranteed to be unique"
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date time the object created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date time the object last updated")

    base_manager = BaseManager()

    class Meta:
        abstract = True
