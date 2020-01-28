"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, matrix_of_list):
        self.matrix_of_list = matrix_of_list

    def __add__(self, other):
        my_list_3 = []
        for i in range(0, len(self.matrix_of_list)):
            my_list_4 = []
            for j in range(0, len(self.matrix_of_list[0])):
                my_list_4.append(self.matrix_of_list[i][j] + other.matrix_of_list[i][j])
            my_list_3.append(my_list_4)
        self.matrix_of_list = my_list_3
        return Matrix(self.matrix_of_list)

    def __str__(self):
        for i in self.matrix_of_list:
            for j in i:
               print(j, end=" ")
            print()
        return ""


matr_1 = Matrix([[1, 2, 3], [4, 5, 6]])
matr_2 = Matrix([[10, 20, 30], [40, 50, 60]])
matr_3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(matr_1)
print(matr_2)
matr_4 = matr_1 + matr_2 + matr_3
print(matr_4)
