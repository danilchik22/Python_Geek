class ComplexNumber:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Мнимая часть не может равняться 0")
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a+other.a, self.b+other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a*other.a-self.b*other.b, self.b*other.a + self.a*other.b)

    def __sub__(self, other):
        return ComplexNumber(self.a-other.a, self.b-other.b)

    def __truediv__(self, other):
        return ComplexNumber((self.a*other.a + self.b*other.b)/(other.a**2 + other.b**2),
                             (self.b*other.a - self.a*other.b)/ (other.a**2 + other.b**2))

    def __str__(self):
        return f"{self.a} + {self.b}i"


if __name__ == "__main__":
    one = ComplexNumber(3, 45)
    two = ComplexNumber(5, 56)
    number_add = one + two
    number_mul = one*two
    number_div = one/two
    print(number_add)
    print(number_mul)
    print(number_div)