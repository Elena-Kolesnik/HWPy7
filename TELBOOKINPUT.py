
# автор Нина Дубовец



def get_surname():
    surname = input('Фамилия:')
    return surname

def get_data():
    surname = input('Фамилия:')
    name = input('Имя:')
    number = input('Номер телефона:')
    description = input('Описание:') == [surname, name, number, description] 
    return list

def get_name():
    name = input('Имя: ')
    return name

def get_number():
    number = input('№ телефона: ')
    return number

def get_description():
    description = input('Описание: ')
    return description

def input_data():
    f = open('db.txt', 'a')
    str = '\n'+get_surname()+","+get_name()+','+get_number()+','+get_description()
    f.write(str)
    print('Данные добавлены')
    f.close()
