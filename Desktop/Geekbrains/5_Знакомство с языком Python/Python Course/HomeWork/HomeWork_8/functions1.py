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

def select_data_person(worker):
    user_lst = []
    a = 1
    with open('book.txt', 'r', encoding='utf-8') as f:
        full_lst = f.readlines()
        for line in full_lst:
            if worker in line:
                user_lst.append(line)
                a += 1
                print(f"{a + 1} {line}")
    return user_lst, full_lst 

def delete_data(user_lst, full_lst, num):
    with open('book.txt', 'w', encoding='utf-8') as f:
        for line in full_lst:
            if user_lst[num - 1] != line:
                f.write(line)
    print('готово')

def get_number():
    num = int(input('Выберите строчку для изменения: '))
    return num

def get_data():
    print('Введите новые данные: ')
    name = input('Имя: ')
    surname = input('Фамилия: ')
    tel = input('Номер телефона: ')
    data_str = name + " " + surname + " " + tel + "\n"
    return data_str

def get_data_worker():
    data = input('Введите новые о пользователе, которые хотите посмотреть: ')
    return data

def change_data(user_lst, full_lst, num, new_worker):
    with open('book.txt', 'w', encoding='utf-8') as f:
        for line in full_lst:
            if user_lst[num - 1] != line:
                f.write(line)
            else:
                f.write(new_worker)
    print('готово')

