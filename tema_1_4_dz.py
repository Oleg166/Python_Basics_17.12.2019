number = int(input("Введите целое положительное число: "))  # запрашиваем число у пользователя
max_number = 0  # объявляем искомую переменную и присваиваем ей значение 0
while number > 0:    # Объявляем цикл while с условием - пока число number больше нуля
    ost = number % 10  # объявляем переменную ost, равную последней цифре в числе
    if ost >= max_number:  # сравниваем последнюю цифру в числе и искомое значение. Если последняя цифра больше -
        max_number = ost  # то искомое значение равно последней цифре
    number == number // 10  # отбрасываем последнюю цифру числа
print(max_number)