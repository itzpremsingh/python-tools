from math import sqrt

a, b, c = 39, 49, 39


class Equation:
    def __init__(self, a, b, c, v="x") -> None:
        self.a = a
        self.b = b
        self.c = c
        self.v = v

    def __str__(self) -> str:
        contSign = "+"
        coefSign = "+"
        v = self.v

        equation = f"{self.a}{v}² <sign_b> {abs(self.b)}{v} <sign_c> {abs(self.c)}"

        if b < 0:
            coefSign = "-"
        if c < 0:
            contSign = "-"

        equation = equation.replace("<sign_b>", coefSign)
        equation = equation.replace("<sign_c>", contSign)

        return equation

    @property
    def canSolve(self) -> bool:
        discriminant: int = self.b**2 - 4 * self.a * self.c

        if discriminant < 0:
            return False
        else:
            return True

    def root(self):
        if not self.canSolve:
            return None
        a = self.a
        b = self.b
        c = self.c

        d = b**2 - 4 * a * c

        root1 = (-b + sqrt(d)) / 2 * a
        root2 = (-b - sqrt(d)) / 2 * a

        return root1, root2


equation = Equation(a, b, c)
print(equation)
