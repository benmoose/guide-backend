import attr


@attr.s(slots=True)
class Location:
    lat = attr.ib()
    lng = attr.ib()

    @classmethod
    def from_dict(cls, data):
        return cls(
            lat=data['lat'],
            lng=data['lng'],
        )


@attr.s(slots=True)
class Place:
    location = attr.ib()
    display_name = attr.ib()
    description = attr.ib()
    display_address = attr.ib()

    @classmethod
    def from_dict(cls, data):
        location = data['location']
        return cls(
            location=Location.from_dict(location) if location is not None else None,
            display_name=data.get('display_name'),
            display_address=data.get('display_address'),
            description=data.get('description'),
        )

    @classmethod
    def safe_from_dict(cls, data):
        try:
            return cls.from_dict(data)
        except KeyError:
            return None
