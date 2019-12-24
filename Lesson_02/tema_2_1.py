"""my_list = ('one', 'two', 'three')
print(' '.join(my_list))
my_str = 'HeLLO WORld!'
print(my_str.title())
print(my_str.capitalize())
print(my_str.lower())
print(my_str.upper())
print(my_str.istitle())
print('e' in my_str)
print(my_str.count('L'))
print(my_str.find('W', 7))

my_tuple = ('Hello', 10, 51.2, True, [1, 2, 3, [5, 6, 7]])
#print(type(my_tuple))
a = '(10)'
b = '(11)'

print(id(a), id(b))
print(a is b)

# my_set = {1, 2, 2, 3, 3, 44, 6, 0 ,7 ,8 ,89}
# print(my_set)
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a == b)
print(a & b)
print(a - b)
print(a ^ b)
#a.remove(3)
print(a)
a.discard(3)
print(a)

human = {'name': 'Ivan', 'surname': 'Ivanov', 'age': 20}
human['data'] = [1, 2, 3, 5]
print(human['name'])
print(human.keys())
print(human.values())
print(human.items())

#print(b'text')
print('текст'.encode('utf-8'))
print('ТЕКСТ'.encode('utf-8'))

try:
    print(10/b)
except ZeroDivisionError:
    print('Деление на ноль!')
except TypeError:
    print('Ошибка неверно введенных данных')
except:
    print('Другая ошибка')

my_str = 'Hello World!'
for i in my_str:
    print(i)

a = 5 if 7 > 6 else 0
print(a)

age = int(input('Age: '))
print(('Welcome' if age > 18 else 'dostup impossible'))
"""
a = ['a', 'b', 'c', 'd']
for i, el in enumerate(a, start=1):
    print(i, el)
