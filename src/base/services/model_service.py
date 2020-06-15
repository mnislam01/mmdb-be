
class BaseModelService:

    model = None
    
    def get_model(self):
        assert not self.model is None, f"{self.__class__} doesnt have a properly set model property."
        return self.model
