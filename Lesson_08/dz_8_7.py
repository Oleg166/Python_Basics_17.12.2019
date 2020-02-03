"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b == 1:
            return f"{self.a}+i"
        elif self.b == -1:
            return f"{self.a}-i"
        elif self.b > 0:
            return f"{self.a}+{self.b}i"
        elif self.b < 0:
            return f"{self.a}{self.b}i"
        elif self.b == 0:
            return f"{self.a}"

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex((self.a*other.a - self.b*other.b), (self.b*other.a + self.a*other.b))


numeric_1 = Complex(5, -3)
numeric_2 = Complex(-1, 2)
print(numeric_1)
print(numeric_2)
numeric_3 = numeric_1+numeric_2
print(numeric_3)
numeric_4 = numeric_1 + numeric_3
print(numeric_4)
numeric_4 = numeric_1-numeric_2
numeric_5 = numeric_2-numeric_1
print(numeric_4)
print(numeric_5)
numeric_6 = numeric_1*numeric_2
print(numeric_6)