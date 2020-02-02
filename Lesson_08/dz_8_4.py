"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники."""


class Sklad:
    """Описывает склад. category - категория складируемой продукции, count - количество"""
    def __init__(self, category, count):
        self.name = category
        self.count = count


class OrgTechnik(Sklad):
    """Описывает оргтехнику. name - название, sn - серийный номер, price - цена"""
    def __init__(self, name, sn, price):
        self.name = name
        self.sn = sn
        self.price = price


class Printer(OrgTechnik):
    """Описывает принтеры. type - тип(струйный, лазерный), color - тип печати(цветной, черно-белый)"""
    def __init__(self, type, color):
        self.type = type
        self.color = color


class Scaner(OrgTechnik):
    """Описывает сканеры. dpi - разрешение сканирования, form - форма(планшетный, поточный)"""
    def __init__(self, dpi, form):
        self.dpi = dpi
        self.form = form


class Kseroks(OrgTechnik):
    """Описывает ксероксы. size - размер(большой, средний, маленький), mfu - является МФУ или нет"""
    def __init__(self, size, mfu):
        self.size = size
        self.mfu = mfu


scan_1 = Scaner(400, 'планшетный')
print(scan_1)