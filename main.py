# autor Sergey Mitroshin

import func1
import Convert1
import view


command=0
exitflag=0
while exitflag==0:
    view.printmenu()
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
        else:
            view.printerror()
    except:
        view.printerror()
    
