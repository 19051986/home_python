# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

a = input('Введите строку текста: ')
word_list = a.split(' ')

for i, word in enumerate(word_list):
    print(f'{i + 1}. {word[0:10]}')
