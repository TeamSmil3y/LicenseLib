class DataContainer:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                setattr(self, key, DataContainer(**value))
            else:
                setattr(self, key, value)

    def __repr__(self):
        attributes = {key: getattr(self, key) for key in dir(self) if not key.startswith('__')}
        return f'DataContainer(**{attributes.__str__()})'
