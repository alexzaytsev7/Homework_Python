# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и
# удаления данных

def add_contact(f):
    input_name = input('Введите Имя: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_last_name}; {input_name}; {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list


def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)


def search_contact(f):
    last_name = input('Введите фамилию для поиска: ')
    adr_book = read_all(f)
    # print(len(adr_book))
    count_index = 0
    for i in range(len(adr_book)):
        if last_name in adr_book[i].split(';')[0]:
            count_index += 1
            print(i, adr_book[i])
            if count_index == 1:
                idx = i
                print(idx)
    if count_index > 1:
        idx = int(input('Введи индекс для замены: '))

    last_name = input('введите новую фамилию: ')
    name = input('введите новое имя: ')
    phone = input('новый номер: ')
    new_record = f'{last_name}; {name}; {phone}'
    adr_book[idx] = new_record
    with open(f, 'w', encoding='utf-8') as fd:
        fd.writelines(adr_book)


def main():
    # user_choice = ''
    # while user_choice != 'z':
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - добавить запись,\n2 - прочитать всю тел.книгу,\n'
                            '3 - найти запись,\nz - для выхода: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == 'z':
            print('Всего хорошего')
            break


if __name__ == '__main__':
    main()
