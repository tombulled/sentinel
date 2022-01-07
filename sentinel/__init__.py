from .meta import SentinelMeta

class Sentinel(SentinelMeta, metaclass=SentinelMeta): pass

# Common sentinels
class Missing(Sentinel): pass
class Default(Sentinel): pass
