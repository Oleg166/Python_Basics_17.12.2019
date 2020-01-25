"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров)."""

class Worker():
    name = "name"
    surname = "surname"
    position = "position"
    _income = {"wage": 0, "bonus": 0}
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": w, "bonus": b}
        # print(f"Имя работника: {n}\nФамилия работника: {s}\nДолжность работника: {p}\nОклад работника: {w}\nПремия работника: {b}")

class Position(Worker):
    def get_full_name(self, n, s, p, w, b):
        print(Worker.name + Worker.surname)
    def get_total_income(self):
        pass

# w_1 = Worker("Вася", "Пупкин", "Директор", 15000, 5000)
# w_2 = Worker("Иннокентий", "Сидоров", "Заместитель директора", 10000, 2000)
# w_1 = Position("Вася", "Пупкин", "Директор", 15000, 5000)
w_1 = Worker()
print(w_1.get_full_name("Вася", "Пупкин", "Директор", 15000, 5000))