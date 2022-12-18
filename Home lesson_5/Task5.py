# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

f = open('Numbers_task5.txt', 'w')
print("Введите набор чисел, разделенных пробелами: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break

f = open('Numbers_task5.txt', 'r')
lst = f.read().split()
total = 0
for elem in lst:
    total += float(elem)
print("Сумма чисел в файле: ", total)
f.close()
