# autor Ilya Kumankov
# поиск по файлу
# def search():
def search():
    searchString = input('Введите поисковый запрос - ').lower()
    with open("db.txt", encoding="utf-8") as inputFile:
        inputdb = [row.strip() for row in inputFile]
        for i in range(len(inputdb)):
            if searchString in inputdb[i].lower():
                print(f'Строка № {i+1} - {inputdb[i]}')
    return