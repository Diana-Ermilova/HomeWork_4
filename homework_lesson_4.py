import pytest
import math
import random

from selenium.webdriver.common.devtools.v136.bluetooth_emulation import add_service


def test_name_age():
    name = "Anna"
    age = "20"
    result = f"Hello {name}, u're {age} yrs old!"

    assert result == "Hello Anna, u're 20 yrs old!"

def test_rectangle(): #эта функция считает прямоугольник
    length = 10
    width = 20
    S = length * width #площадь
    P = (length+width)*2 #периметр

    assert S == 200
    assert P == 60

def test_circle(): #эта функция считает круг
    radius = 4

    length = 2*math.pi*radius #длина окружности
    area = (radius**2)*math.pi #площадь

    assert length == 25.132741228718345
    assert area == 50.26548245743669

def test_list(): #функция создает рандомный сортированный список
    L = [random.randint(1, 100) for _ in range(10)]
    L.sort()

    assert len(L) == 10
    assert all(L[i] <= L[i + 1] for i in range(len(L) - 1))

def test_remove_repeat(): #функция проверяет список на уникальность
    LRepeats = [1, 1, 2, 1, 1, 3, 3, 4, 5, 6, 6, 12, 12, 13, 9, 8, 8]
    LUnique = []
    for i in LRepeats:
        if i not in LUnique:
            LUnique.append(i)
    assert LUnique == [1, 2, 3, 4, 5, 6, 12, 13, 9, 8]

def test_repeate_set(): #дополнительно еще через set(), уменьшение временной сложности
    LRepeat = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7]
    SUniqie = set()
    LUnique = []
    for i in LRepeat:
        if i not in SUniqie:
            SUniqie.add(i)
            LUnique.append(i)
    assert LUnique == [1, 2, 3, 4, 5, 6, 7]

def test_dict(): #функция создает словарь
    keys = [1, 2, 3, 4, 5]
    values = ['ham', 'spam', 'eggs', 'bread', 'circus'] #hello to Mark Lutz
    Z = zip(keys, values)
    D = dict(Z)
    assert isinstance(D, dict)
    assert len(D) == 5
    assert list(D.keys()) == keys
    assert list(D.values()) == values