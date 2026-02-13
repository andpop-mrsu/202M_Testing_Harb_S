import pytest
from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides


def test_valid_triangle():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12


def test_equilateral_triangle():
    t = Triangle(5, 5, 5)
    assert t.triangle_type() == "equilateral"


def test_isosceles_triangle():
    t = Triangle(6, 6, 8)
    assert t.triangle_type() == "isosceles"


def test_invalid_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 10)


def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 2, 2)
