"""Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""


def my_func(x, y):
    return print(x**y)


def my_func_1(q, w):
    for_infinite_cycle = 0
    counter = 0
    result = 1
    if w == 0:
        print(1)
    else:
        ww = abs(w)
        while for_infinite_cycle != 1:
            result = result * q
            counter += 1
            if counter == ww:
                if w > 0:
                    print(result)
                elif w < 0:
                    print(1/result)
                break


my_func(2, -1)
my_func_1(2, -1)

