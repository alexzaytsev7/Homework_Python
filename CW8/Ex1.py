with open('file.txt', 'w', encoding='utf-8') as fd:
    fd.write('первая строка в файле')
with open('file.txt', 'a', encoding='utf-8') as fd:
    fd.write('\nвторая строка в файле')

with open('file.txt', 'r', encoding='utf-8') as fd:
    #z = fd.read()
    z = fd.readlines()
    for i in z:
        print(i)
    #print(z)

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
        print(fd.read())

def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)

def serch_contact(f):
    last_name = input('Введите фамилию для поиска: ')
    adr_book = read_all(f)
    for line in adr_book:
        if last_name in line:
            print(line)

def main():
    # user_choice = ''
    # while user_choice != 'z':
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - добавить запись, 2 - прочитать всю тел.книгу, 3 - найти запись, z - для выхода: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            read_all(file)
        elif user_choice == '3':
            serch_contact(file)
        elif user_choice == 'z':
            print('Всего хорошего')
            break

if __name__ == '__main__':
    main()



