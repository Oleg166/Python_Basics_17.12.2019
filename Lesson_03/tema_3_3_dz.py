"""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов."""
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))


def my_func(a, b, c):
    max_of_three = max(a, b, c)
    min_of_three = min(a, b, c)
    middle = a + b + c - max_of_three - min_of_three
    return print(max_of_three + middle)


my_func(x, y, z)