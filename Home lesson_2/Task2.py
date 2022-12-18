# Для списка реализовать обмен значений соседних элементов, т.е. значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

element_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
elem = 0
while i < element_count:
    my_list.append(input("Введите значение списка "))
    i += 1
for element in range(int(len(my_list) / 2)):
    my_list[elem], my_list[elem + 1] = my_list[elem + 1], my_list[elem]
    elem += 2
print(my_list)
