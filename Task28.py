# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


data_file = open("salary_task28.txt", "r")
sotrudniki_count = 0
sotrudniki_sum = 0
for line in data_file.readlines():
    sotrudniki_count += 1
    sotrudniki_sum += float(line.split()[1])
    if float(line.split()[1]) < 20000:
        print(line.split()[0])
print(f"Средний доход: {sotrudniki_sum / sotrudniki_count}")
data_file.close()
