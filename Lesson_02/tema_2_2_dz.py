"""Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2
и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input()."""
my_list = []
a = None
while a != 'stop':
    a = input("Введите элемент списка (для вывода результата введите stop): ")
    if a == 'stop':
        break
    else:
        my_list.append(a)
j = 0
for i in range(int(len(my_list)/2)):
    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    j += 2
print(my_list)