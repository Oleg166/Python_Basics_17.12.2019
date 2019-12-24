day = 17
month = 'декабря'
year = '2019'
print('Это задание выполнено {} {} {} года.\n'.format(day, month, year))

day_user = int(input("Какой сегодня день месяца (введите число): "))
month_user = input("Какой сейчас месяц: ")
year_user = int(input("Какой сейчас год (введите цифрами): "))
print('\nВы указали дату:\n'
      'число: {}\n'
      'месяц: {}\n'
      'год: {}'.format(day_user, month_user, year_user))
