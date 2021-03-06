"""Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра."""


class Stationery:
    def __init__(self):
        self.title = "Название"

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def draw(self):
        return "Запуск рисования ручкой"


class Pencil(Stationery):
    def draw(self):
        return "Запуск рисования карандашом"


class Handle(Stationery):
    def draw(self):
        return "Запуск рисования маркером"


abc = Stationery()
pen_1 = Pen()
pencil_1 = Pencil()
handle_1 = Handle()
print(abc.draw())
print(pen_1.draw())
print(pencil_1.draw())
print(handle_1.draw())
