import pytest
from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides

def test_triangle_create_ok():
    t = Triangle(3, 4, 5)
    assert t.perimeter() == 12
    assert t.triangle_type() == "nonequilateral"

def test_triangle_equilateral():
    t = Triangle(2, 2, 2)
    assert t.triangle_type() == "equilateral"

def test_triangle_invalid():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)
