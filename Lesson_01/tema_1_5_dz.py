revenue = int(input("Введите значение выручки фирмы: "))
costs = int(input("Введите значение издержек фирмы: "))
result = abs(revenue - costs)
if revenue > costs:
    print("Фирма работает с прибылью. Прибыль составляет: {}.".format(result))
    rent = result/revenue * 100
    rent = round(rent, 2)
    print("Рентабельность фирмы составляет: {} %.".format(rent))
    staff = int(input("Введите численность сотрудников фирмы: "))
    result_for_staff = result / staff
    result_for_staff = round(result_for_staff, 2)
    print("Размер пибыли на одного сотрудника составляет {}.".format(result_for_staff))
elif revenue < costs:
    print("Фирма работает в убыток. Убыток составляет: {}.".format(result))

