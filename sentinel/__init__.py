__all__ = ['SentinelMeta', 'Sentinel', 'Missing']

class SentinelMeta(type):
    """ Metaclass for Sentinel """

    def __new__(metaclass, name, bases, namespace):
        def __new__(cls, *args, **kwargs):
            raise TypeError(f'type {cls.__name__!r} is not an acceptable base type')

        def __setattr__(cls, name, value):
            raise AttributeError(f'{cls.__name__!r} object has no attribute {name!r}')

        def __getattr__(cls, name):
            raise AttributeError(f'{cls.__name__!r} object has no attribute {name!r}')

        namespace['__new__']     = __new__
        namespace['__setattr__'] = __setattr__
        namespace['__getattr__'] = __getattr__

        cls = super().__new__(metaclass, name, bases, namespace)

        super().__setattr__(cls, '__class__', cls)

        return cls

    def __repr__(cls):
        return cls.__name__

class Sentinel(SentinelMeta, metaclass=SentinelMeta): pass

# Allow subclassing
del Sentinel.__new__

class MISSING(Sentinel): pass
