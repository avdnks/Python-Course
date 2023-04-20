def show_data() -> None:
    #Выводит информацию из справочника
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    #Добавляет информацию в справочник
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')

def find_data() -> None:
    #Осуществляет поиск по справочнику
    data = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска: ')
    print(search(tel_book, data))

def search(book: str, info: str) -> str:
    #Находит в строке записи по определенному критерию поиска
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

