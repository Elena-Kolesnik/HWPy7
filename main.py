# autor Sergey Mitroshin
# main module 

import func1
import Convert1
import view
import TELBOOKINPUT


command=0
exitflag=0
while exitflag==0:
    view.printmenu()
    try:
        command =int(input())
        if command==1:
            TELBOOKINPUT.input_data()
        elif command == 2:
            func1.fun1()
            exitflag = 1 # если хотим завершить программу
        elif command == 0:
            exitflag = 1
        elif command == 3:
            Convert1.Convert()
            view.conv1ok()
            exitflag = 1
        else:
            view.printerror()
    except:
        view.printerror()
    
