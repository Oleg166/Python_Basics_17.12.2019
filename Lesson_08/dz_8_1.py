"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Data:
    def __init__(self, param):
        self.param = param

    @classmethod
    def first(cls, param):
        day = int(param[0:2])
        month = int(param[3:5])
        year = int(param[6:])
        print(f'Число: {type(day)}. Месяц: {type(month)}. Год: {type(year)}.')
        # print(f'Число: {day}. Месяц: {month}. Год: {year}.')

    @staticmethod
    def two(param):
        if 1 <= int(param[0:2]) <= 31:
            # a = True
            print('День указан верно')
        else:
            # a = False
            print('День указан неверно')
        if 1 <= int(param[3:5]) <= 12:
            # b = True
            print('Месяц указан верно')
        else:
            # b = False
            print('Месяц указан неверно')
        if 1 <= int(param[6:]) <=9999:
            # c = True
            print('Год указан верно')
        else:
            # c = False
            print('Год указан неверно')



# Data.first('25-12-2018')
mc = Data
mc.first('25-12-2018')
mc.two('25-12-2018')
mc.two('00-00-0000')
