class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
    """
    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 3, 2)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    """
    sides = sorted([a, b, c])
    if sides[0] <= 0 or sides[0] + sides[1] <= sides[2]:
        raise IncorrectTriangleSides("Invalid triangle sides")

    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"
