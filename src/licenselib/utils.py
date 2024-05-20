class DataContainer:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                setattr(self, key, DataContainer(**value))
            else:
                setattr(self, key, value)

    def __repr__(self):
        attributes = {}
        for key in dir(self):
            value = getattr(self, key)
            if not key.startswith('_') and not callable(value):
                print(4, key, value)
                attributes[key] = value
        return f'{type(self).__name__}(**{attributes.__str__()})'
