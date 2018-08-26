import attr


def data_model(cls):
    """
    Decorator which adds useful serialisation methods for data models.
    """
    if not hasattr(cls, 'to_dict'):
        cls.to_dict = attr.asdict

    if not hasattr(cls, 'from_dict'):
        cls.from_dict = classmethod(from_dict)

    if not hasattr(cls, 'safe_from_dict'):
        cls.safe_from_dict = classmethod(safe_from_dict)

    cls.__data_object__ = True

    return attr.s(
        cls,
        these=get_attr_ib_dict(cls.__slots__),
        hash=True,
        slots=True,
    )


def get_attr_ib_dict(slots):
    output = {}
    for field in slots:
        output[field] = attr.ib(default=None)
    return output


def get_slots_from_fields(cls):
    return tuple(lambda f: f.name, attr.fields(cls))


def from_dict(cls, data):
    obj = cls()
    for field in cls.__slots__:
        value = data.get(field)
        if value is not None:
            setattr(obj, field, value)
    return obj


def safe_from_dict(cls, data):
    try:
        return cls.from_dict(data)
    except (KeyError, TypeError):
        return None
