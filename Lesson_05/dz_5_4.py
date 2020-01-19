"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл"""
my_f = open("numbers_5_4.txt", "r")
content = my_f.readline()
content = content[:-1]  # удаляем символ переноса строки
with open("numbers_answer_5_4.txt", "w") as f_obj:
    print(content.replace('One', 'Один'), file=f_obj)

content = my_f.readline()
content = content[:-1]  # удаляем символ переноса строки
with open("numbers_answer_5_4.txt", "a") as f_obj:
    print(content.replace('Two', 'Два'), file=f_obj)

content = my_f.readline()
content = content[:-1]  # удаляем символ переноса строки
with open("numbers_answer_5_4.txt", "a") as f_obj:
    print(content.replace('Three', 'Три'), file=f_obj)

content = my_f.readline()
with open("numbers_answer_5_4.txt", "a") as f_obj:
    print(content.replace('Four', 'Четыре'), file=f_obj)
