"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран."""
n = None
in_f = open('answer_5_5.txt', 'w')
while n != "":
    n = input("Введите число, которое хотите записать(пеустая строка - прекратить ввод): ")
    if n == "":
        break
    with open("answer_5_5.txt", "a") as f_obj:
        print(n, file=f_obj)
out_f = open('answer_5_5.txt', 'r')
numbers = out_f.readlines()
out_f.close()
result = 0
for i in numbers:
    result = result + int(i)
print(f"Сумма чисел в файле: {result}")
in_f = open('answer_5_5.txt', 'a')
in_f.write("Сумма чисел в файле: " + str(result))
in_f.close()
