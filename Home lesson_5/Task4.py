# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.

slovarj = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

input_file = open("tekst_task4.txt")
out_file = open("tekst2_task4.txt", "a", encoding="utf8")

for line in input_file.readlines():
    for slovo in slovarj:
        if slovo == line.split()[0]:
            line = line.replace(line.split()[0], slovarj.get(slovo))
            out_file.write(f"{line}")
            print(line)

input_file.close()
out_file.close()
