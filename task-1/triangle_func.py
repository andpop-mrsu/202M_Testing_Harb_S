class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass


def get_triangle_type(a, b, c):
    """
    Возвращает тип треугольника:
    "nonequilateral", "isosceles", "equilateral".

    Примеры (doctest):

    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 3, 5)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(1, 1, 10)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides
    """

    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise IncorrectTriangleSides

    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides

    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides

    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
