"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
import time
from itertools import cycle


class TrafficLight():
    def __init__(self):
        self.__color = None
    def running(self, color):
        if color == 'red' and (self.__color == 'green' or self.__color == None):
            self.__color = color
            print('горит красный')
            time.sleep(7)
        elif color == 'yellow' and self.__color == 'red':
            self.__color = color
            print('горит желтый')
            time.sleep(2)
        elif color == 'green' and self.__color == 'yellow':
            self.__color = color
            print('горит зеленый')
            time.sleep(5)
        else:
            print('Ошибка последовательности')
a = TrafficLight()
a.running('red')
a.running('yellow')
a.running('green')
a.running('red')
a.running('yellow')
a.running('green')
a.running("yellow")
"""
c = 0
for el in cycle(print(TrafficLight())):
    if c > 2:
        break
    c += 1"""