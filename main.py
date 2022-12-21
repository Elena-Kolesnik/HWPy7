# autor Sergey Mitroshin

import func1
import Convert1

command=0
exitflag=0
while exitflag==0:
    print ('*************************************')
    print (' Текстовая база телефонов')
    print (' Нажмите: ')
    print ('1 Для ввода данных в базу')
    print ('2 Для вызова функции 1')
    print ('3 Для конвертации базы в формат 1')
    print ('0 Для завершения программы')
    print ('*************************************')
    try:
        command =int(input())
        if command==1:
            print('1 ok')
        elif command == 2:
            func1.fun1()
            exitflag = 1 # если хотим завершить программу
        elif command == 0:
            exitflag = 1
        elif command == 3:
            Convert1.Convert()
            print('База сконвертирована в файл convert1.txt')
            exitflag = 1
    except:
        print ('Неправильный ввод! Пожалуйста,повторите: ')

    
