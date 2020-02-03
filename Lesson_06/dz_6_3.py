"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров)."""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        result = self._income.setdefault("wage") + self._income.setdefault("bonus")
        return f"Полный доход сотрудника {self.name} {self.surname} составляет {result}."


w_1 = Position("Вася", "Пупкин", "Директор", 15000, 5000)
w_2 = Position("Иннокентий", "Сидоров", "Заместитель директора", 10000, 2000)
print(w_1.get_full_name())
print(w_2.get_full_name())
print(w_1.get_total_income())
print(w_2.get_total_income())