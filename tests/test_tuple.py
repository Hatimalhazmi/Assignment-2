import pytest

from mypkg.my_answers import tuple

x, y, z, f, m, n = tuple()


def test_1():
    assert(x == 11)


def test_2():
    assert(y == 1000)


def test_3():
    assert(z == 7)


def test_4():
    assert(f == 2)


def test_5():
    assert(m == 10148)


def test_6():
    assert(n == 8679)
