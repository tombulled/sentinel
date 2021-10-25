from . import base

class Default (base.Sentinel): pass
class Deleted (base.Sentinel): pass
class Empty   (base.Sentinel): pass
class Finished(base.Sentinel): pass
class Found   (base.Sentinel): pass
class Missing (base.Sentinel): pass
class NotSet  (base.Sentinel): pass
class Null    (base.Sentinel): pass
class Unknown (base.Sentinel): pass
