"""Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь."""


class Sklad:
    """Описывает склад. category - категория складируемой продукции, count - количество"""
    def __init__(self, category, count):
        self.category = category
        self.count = count

    def coming(self):
        pass

    def outgo(self, otdel):
        pass


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
