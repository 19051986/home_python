# Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
# оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали
# и чего удалось добиться.

from random import randint
from memory_profiler import profile


@profile
def my_function():
    """Функция сравнения элементов списка"""
    my_list = [randint(0, 10000) for i in range(1000)]
    new_lst = []
    for elm in range(int(len(my_list) - 1)):
        if my_list[elm + 1] > my_list[elm]:
            new_lst.append(my_list[elm + 1])
            elm += 1
    return new_lst


@profile
def my_function_2():
    """Удаление генерируемого списка приводит к уменьшению выделяемой памяти"""
    my_list = [randint(0, 10000) for i in range(100000)]
    new_lst = []
    for elm in range(int(len(my_list) - 1)):
        if my_list[elm + 1] > my_list[elm]:
            new_lst.append(my_list[elm + 1])
            elm += 1
    del my_list
    return new_lst


@profile
def my_function_3():
    """При использовании генератора "yield" мы не видим выделения памяти"""
    my_list = [randint(0, 100) for i in range(10)]
    new_lst = []
    for elm in range(int(len(my_list) - 1)):
        if my_list[elm + 1] > my_list[elm]:
            new_lst.append(my_list[elm + 1])
            elm += 1
    print(new_lst)
    yield new_lst


my_function()
my_function_2()
next(my_function_3())


@profile
def my_func():
    """ Изменил вводные данные для наглядности отображения"""
    numbers = [randint(0, 1000) for i in range(100000)]
    new_list = [el for el in numbers if el % 100 == 0]
    return new_list


@profile
def my_func_2():
    """Присвоил списку значение None"""
    numbers = [randint(0, 1000) for i in range(100000)]
    new_list = [elm for elm in numbers if elm % 100 == 0]
    numbers = None
    return new_list


my_func()
my_func_2()
