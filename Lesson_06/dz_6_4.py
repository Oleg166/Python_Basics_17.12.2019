"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f"Автомобиль {self.name} поехал."

    def stop(self):
        return f"Автомобиль {self.name} остановился."

    def turn(self, direction):
        return f"Автомобиль {self.name} повернул {direction}."

    def show_speed(self):
        return f"Скорость автомобиля {self.name} составляет {self.speed} км/ч."


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Скорость автомобиля {self.name} составляет {self.speed} км/ч. Превышена максимальная разрешенная скорость"
        else:
            return f"Скорость автомобиля {self.name} составляет {self.speed} км/ч. "


class SportCar(Car):
    # спортивный автомобиль
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Скорость автомобиля {self.name} составляет {self.speed} км/ч. Превышена максимальная разрешенная скорость"
        else:
            return f"Скорость автомобиля {self.name} составляет {self.speed} км/ч. "


class PoliceCar(Car):
    # полицейский автомобиль
    def definition(self):
        if self.is_police == True:
            return "Это полицейский автомобиль"
        else:
            return "Это не полицейский автомобиль"


car_tesla = SportCar("Тесла", "Красный", 90, False)
print(car_tesla.go())
print(car_tesla.turn("направо"))
print(car_tesla.stop())
print(car_tesla.show_speed())
print()
car_renault = TownCar("Рено", "Синий", 59, False)
print(car_renault.show_speed())
print()
car_tracktor = WorkCar("Трактор", "Зеленый", 45, False)
print(car_tracktor.show_speed())
print()
car_ford_police = PoliceCar("Форд", "Белый", 100, True)
print(car_ford_police.definition())
