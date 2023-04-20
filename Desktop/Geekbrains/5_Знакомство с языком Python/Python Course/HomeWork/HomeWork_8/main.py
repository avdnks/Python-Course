# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может 
# ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import functions1

while True :
    print('1. Ввод, 2. Добавление, 3. Поиск, 4. Изменение, 5. Удаление')
    mode = int(input())
    if mode == 1:
        functions1.show_data()
    elif mode == 2:
        functions1.add_data()
    elif mode == 3:
        functions1.find_data()
    elif mode == 4:
        data_str = functions1.get_data_worker()
        user_lst, full_lst = functions1.select_data_person(data_str)  
        num = functions1.get_number()
        new_worker = functions1.get_data()
        functions1.change_data(user_lst, full_lst, num, new_worker)
    elif mode == 5:
        data_str = functions1.get_data_worker()
        user_lst, full_lst = functions1.select_data_person(data_str)  
        num = functions1.get_number()
        functions1.delete_data(user_lst, full_lst, num)
    else:
        print('Выход')
        break