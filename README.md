# sentinel
Implementation of the Sentinel Object Pattern

## Prelude
Come voice your opinions on [PEP-661](https://www.python.org/dev/peps/pep-0661/) (adding official sentinel support to the standard library) at [Discussions on Python.org](https://discuss.python.org/t/pep-661-sentinel-values/9126/85)

## Usage
```python
>>> import sentinel
>>>
>>> class NotFound(sentinel.Sentinel): pass
>>>
>>> NotFound
NotFound
>>>
>>> NotFound is NotFound
True
```
