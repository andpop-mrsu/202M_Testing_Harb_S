from triangle_func import IncorrectTriangleSides

class Triangle:
    def __init__(self, a, b, c):
        sides = sorted([a, b, c])
        if sides[0] <= 0 or sides[0] + sides[1] <= sides[2]:
            raise IncorrectTriangleSides("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.a + self.b + self.c
