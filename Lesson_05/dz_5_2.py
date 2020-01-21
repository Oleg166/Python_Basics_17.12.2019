"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""
my_f_1 = open("text_1.txt", "r")
content = my_f_1.readlines()
my_f_1.close()
print("\nВсего строк в файле: " + str(len(content)) + " шт.")
b = []
i = 1
for j in content:
    b = j.split()
    print(f"В {i}-ой строке {len(b)} слов.")
    i += 1

"""with open("text_1.txt") as f:
    lines = f.readlines()
    print('Количество строк: ', len(lines))
    for num_line, line in enumerate(lines, start=1):
        print('{} строка содержит - {} слов'.format(num_line, len(line.split())))"""


