"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""
title_predmet = []  # список со значениями названий предметов
hours = []  # список со значениями часов предметов
result = 0
with open("question_5_6.txt") as f_obj:
    for line in f_obj:
        data_from_file = line.split()
        t = data_from_file[0]
        title_predmet.append(t[:-1])
        data_from_file = data_from_file[1:]
        for i in data_from_file:
            if i.endswith('(л)'):
                result = result + int(i.replace('(л)', ''))
            elif i.endswith('(пр)'):
                result = result + int(i.replace('(пр)', ''))
            elif i.endswith('(лаб)'):
                result = result + int(i.replace('(лаб)', ''))
            else:
                result = result + 0
        hours.append(result)
        result = 0

my_dict = dict(zip(title_predmet, hours))
print(my_dict)
