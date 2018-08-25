from guide.common import data_model

from ..models.place import Place as DBPlace


@data_model
class Location:
    __slots__ = (
        'lat',
        'lng',
    )


@data_model
class Place:
    __slots__ = (
        'location',
        'display_name',
        'display_address',
        'description',
    )

    @classmethod
    def from_dict(cls, data):
        return cls(
            location=Location.from_dict(data['location']),
            display_name=data['display_name'],
            display_address=data['display_address'],
            description=data.get('description'),
        )

    @classmethod
    def from_db_model(cls, db_model):
        return cls(
            location=Location(lat=db_model.lat, lng=db_model.lng),
            display_name=db_model.display_name,
            display_address=db_model.display_address,
            description=db_model.description,
        )

    def to_db_model(self):
        return DBPlace(
            lat=self.location.lat,
            lng=self.location.lng,
            display_name=self.display_name,
            display_address=self.display_address,
            description=self.description,
        )
