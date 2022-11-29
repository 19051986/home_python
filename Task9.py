# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
# времени года относится месяц (зима, весна, лето, осень). Напишите решения
# через list и через dict.

month_dict = {'Зима': [12, 1, 2],
              'Весна': [3, 4, 5],
              'Лето': [6, 7, 8],
              'Осень': [9, 10, 11]}

month_num = int(input('Введите номер месяца (1..12): '))
if month_num in range(1, 13):
    for i in month_dict.items():
        if month_num in i[1]:
            print(f'Время года {i[0]}')
            break
else:
    print('Нет такого месяца!')

month_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8],
              ['Осень', 9, 10, 11]]

month_num = int(input('Введите номер месяца (1..12): '))
if month_num in range(1, 13):
    for i, el in enumerate(month_list):
        if month_num in el[1:4]:
            print(f'Время года {el[0]}')
            break
else:
    print('Нет такого месяца!')
