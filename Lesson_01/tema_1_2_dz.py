time_user = int(input("Введите время в секундах: "))

hours = time_user // 3600  # количество часов - результат целочисленного деления на количество секунд в часе (3600)
minutes = (time_user - hours * 3600) // 60
"""количество минут - результат целочисленного деления на 60 (количество секунд в минуте) разности всего секунд и 
количества секунд в целых часах (количество часов умножить на 3600)"""
second = time_user % 60  # вычисляем количество секунд как остаток от целочисленного деления на 60

print('{}:{}:{}'.format(hours, minutes, second))
