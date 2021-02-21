import pytest

from mypkg.my_answers import tuple

x, y, z, f, m, n = tuple()


def test_1():
    assert(x == 4120900)


def test_2():
    assert(y == "Python")


def test_3():
    assert(len(z) == 10 * len("Python"))


def test_4():
    assert(length == 60)


def test_5():
    assert(m == "Python is Great")


def test_6():
    assert(n == "Python is good")
