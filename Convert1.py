# Ответственный Чуркин Петр

# Модуль конверсии телефонной книги
# Ввод
# Иванов,Иван,23456,закадычный друган
# Вывод
# 1) Иванов,Иван,23456,закадычный друган

# (Формат1) :
# Нумерованный список

def Convert():
    input_file = open("db.txt", "r")
    output_file = open("convert1.txt", "w")
    for i, line in enumerate(input_file, 1):
        output_file.write(f"{i}) {line}")
    input_file.close()
    output_file.close()
    



