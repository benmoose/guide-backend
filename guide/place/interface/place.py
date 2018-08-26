from ..models.place import Place as DBPlace
from ..data_models.place import Place


def get_all_places():
    db_places = DBPlace.objects.all()
    return _db_models_to_data_models(Place, db_places)


def create_place(
    lat,
    lng,
    display_name,
    display_address,
    description='',
):
    place = Place(
        lat=lat,
        lng=lng,
        display_name=display_name,
        display_address=display_address,
        description=description,
    )
    db_model = place.to_db_model()
    db_model.save()  # db_model now has a pk
    return Place.from_db_model(db_model)


def _db_models_to_data_models(cls, db_models):
    return map(lambda db: _db_model_to_data_model(cls, db), db_models)


def _db_model_to_data_model(cls, db_model):
    return cls.from_db_model(db_model)
