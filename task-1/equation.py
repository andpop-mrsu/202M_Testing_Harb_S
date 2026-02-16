import math

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("a must not be 0")
    d = b*b - 4*a*c
    if d < 0:
        return []
    elif d == 0:
        x = -b / (2*a)
        return [x]
    else:
        sqrt_d = math.sqrt(d)
        x1 = (-b - sqrt_d) / (2*a)
        x2 = (-b + sqrt_d) / (2*a)
        return sorted([x1, x2])
