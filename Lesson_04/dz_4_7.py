"""Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""
from math import factorial

def fibo_gen(n):
    for el in range(0, n+1):
        yield factorial(el)


for el in fibo_gen(15):
    print(el)