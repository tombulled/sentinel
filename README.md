# sentinel
Pythonic implementation of the Sentinel Object Pattern

## Usage

### Custom Sentinels
```python
>>> import sentinel
>>>
>>> class NotFound(sentinel.Sentinel): pass
>>>
>>> # Example usage
>>> def find(string, substring):
        if substring in string:
            return string.index(substring)
        return NotFound
>>>
>>> find('Python', 'Py')
0
>>> find('Python', 'Foo')
<NotFound>
>>>
```

### Predefined Sentinels
```python
>>> import sentinel
>>>
>>> # Use dir(sentinel) to view available predefined sentinels
>>>
>>> # Use a predefined sentinel
>>> def hello(name = sentinel.NotSet):
        print(f'Hello, {name}!')
>>>
>>> hello('Sam')
Hello, Sam!
>>> hello()
Hello, <NotSet>!
>>>
```

### Important Concepts
```python
>>> import sentinel
>>>
>>> # Sentinels are classes
>>> isinstance(sentinel.Missing, type)
True
>>>
>>> # Sentinels cannot be initialised
>>> sentinel.Missing()
SentinelInitialisationError: Sentinels cannot be instantiated
>>>
>>> # Sentinels are immutable
>>> sentinel.Missing.foo = 'bar'
SentinelMutationError: Sentinels are immutable
>>>
>>> # Sentinels can (and should) be compared using the 'is' operator
>>> sentinel.Missing is sentinel.Missing
True
>>>
```
