import time

class TestClass(object):
    """docstring for ."""
    def __init__(self, name, yearofbirth, mounthofbith, dayofbith):
        super(TestClass, self).__init__()
        self.fname = name
        self.born = yearofbirth
        self.born1 = mounthofbith
        self.born2 = dayofbith
    def vozrast(self):
        self.year = int(time.strftime('%Y'))
        self.mounth= int(time.strftime('%m'))
        self.day = int(time.strftime('%d'))
        if (self.mounth >= self.born1):
            if(self.day >= self.born2):
                self.age = self.year - self.born

        else:
            self.age = int(self.year) - self.born - 1

        self.ret = self.age
        return self.ret
    def bio(self):
        return self.fname, self.vozrast()



Ivan = TestClass('Ivan', 1999, 7, 2)
Sasha = TestClass('Sasha', 1976, 7, 14)

print(Ivan.bio())
print(Sasha.bio())