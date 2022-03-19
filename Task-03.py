# Задача 3. Контакты

def enter_iter():
    while True:
        count = input('Введите планируемое количество контактов: ')
        if not count.isdigit():
            print('Ошибка в количестве. Ожидается ввод только цифр.')
        else:
            return int(count)


def print_contact(phonebook_dict):
    print('Текущие контакты на телефоне:')
    contact = ''
    if len(phonebook_dict) == 0:
        print('<Пусто>')
    else:
        for contact in phonebook_dict:
            print('{0}\t \t{1}'.format(contact, phonebook_dict[contact]))
    print()


def enter_name():
    while True:
        name = input('Введите имя: ')

        if not name.isalpha():
            print('Ошибка в имени. Имя должно содержать только буквы.')
        elif name in phones_directory:
            print('Ошибка: такое имя уже существует.')
        else:
            return name


def enter_number():
    while True:
        phone = input('Введите номер: ')
        if not phone.isdigit():
            print('Ошибка в номере. Номер должен содержать только цифры.')
        else:
            return phone


phones_directory = dict()

for i in range(enter_iter()):
    print_contact(phones_directory)
    contact_name = enter_name()
    contact_number = enter_number()
    phones_directory[contact_name] = contact_number

print_contact(phones_directory)
