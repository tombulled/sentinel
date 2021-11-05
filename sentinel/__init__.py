__all__ = ['SentinelMeta', 'Sentinel', 'Missing']

class _SentinelMeta(type):
    """ Metaclass for Sentinel """

    def __new__(metaclass, name, bases, namespace):
        def __new__(cls, *args, **kwargs):
            raise TypeError(f'cannot initialise or subclass sentinel {cls.__name__!r}')

        cls = super().__new__(metaclass, name, bases, namespace)

        # We are creating a sentinel, neuter it appropriately
        if type(metaclass) is metaclass:
            cls_call = getattr(cls, '__call__', None)
            metaclass_call = getattr(metaclass, '__call__', None)

            # If the class did not provide it's own `__call__`
            # and therefore inherited the `__call__` belongining
            # to it's metaclass, get rid of it.
            # This prevents sentinels inheriting the Functional API.
            if cls_call is not None and cls_call is metaclass_call:
                cls.__call__ = super().__call__

            # Neuter the sentinel's `__new__` to prevent it
            # from being initialised or subclassed
            cls.__new__ = __new__

        # Sentinel classes must derive from their metaclass,
        # otherwise the object layout will differ
        if not issubclass(cls, metaclass):
            raise TypeError(f'{metaclass.__name__!r} must also be derived from when provided as a metaclass')

        cls.__class__ = cls

        return cls

    def __call__(cls, name, bases=None, namespace=None, /, *, repr=None):
        # Attempts to subclass/initialise derived classes will end up
        # arriving here.
        # In these cases, we simply redirect to `__new__`
        if bases is not None:
            return cls.__new__(cls, name, bases, namespace)

        bases = (cls,)
        namespace = {}

        # If a custom `repr` was provided, create an appropriate
        # `__repr__` method to be added to the sentinel class
        if repr is not None:
            def __repr__(cls):
                return repr

            namespace['__repr__'] =__repr__

        return cls.__new__(cls, name, bases, namespace)

    def __repr__(cls):
        return cls.__name__

class Sentinel(_SentinelMeta, metaclass=_SentinelMeta): pass

class Missing(Sentinel): pass
