"""Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове."""
str_user = 'oneoneoneqzxcvbnm two three four fivefivefive 123456789 0123456789 01234567891'
list_user = str_user.split()

for i, el in enumerate(list_user, start=1):
    if len(list_user[i-1]) > 10:
        str_little = list_user[i-1]
        print(i, str_little[0:10])
    else:
        print(i, el)
