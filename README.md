# sentinel
Implementation of the Sentinel Object Pattern

## Prelude
Come voice your opinions on [PEP-661](https://www.python.org/dev/peps/pep-0661/) (adding sentinels to the standard library) at [Discussions on Python.org](https://discuss.python.org/t/pep-661-sentinel-values/9126/85)

## Usage

### Standard API
```python
import sentinel

class NotFound(sentinel.Sentinel): pass
```

```python
>>> NotFound
NotFound
```

### Functional API
```python
import sentinel

Unspecified = sentinel.Sentinel('Unspecified')
```

```python
>>> Unspecified
Unspecified
```

### Custom Sentinels
```python
import sentinel

class SentinelMeta(sentinel.SentinelMeta):
    def __repr__(self) -> str:
        return f'<{type(self).__name__}>'

class Sentinel(SentinelMeta, metaclass=SentinelMeta): pass

class Example(Sentinel): pass
```

```python
>>> Example
Example
```