import math
import pytest
from string import ascii_lowercase

class BadData(Exception):
    pass

def greet(age, name):
    try:
        age = int(age)
    except:
        raise BadData
    if age < 0 or age > 100:
        raise BadData("Столько не живут")
    if set(name.lower()) - set(ascii_lowercase):
        raise BadData("bad name")
    return f"Hello, {name}, you are {age} old"

def test_name():
    result = greet(23, "fsff")
    assert result == "Hello, fsff, you are 23 old"
    with pytest.raises(BadData):
        result = greet("6000", "fsff")
    with pytest.raises(BadData):
        result = greet("22", "22")

#а теперь дз


