phonebook = {}

def add_contact(name, phone):
    """Добавление контакта в телефонную книгу"""
    phonebook[name] = phone
    update_file()

def update_contact(name, new_phone):
    """Обновление номера телефона для существующего контакта"""
    if name in phonebook:
        phonebook[name] = new_phone
        update_file()
    else:
        print(f"{name} не найден в телефонной книге.")

def delete_contact(name):
    """Удаление контакта из телефонной книги"""
    if name in phonebook:
        del phonebook[name]
        update_file()
    else:
        print(f"{name} не найден в телефонной книге.")

def print_phonebook():
    """Печать содержимого телефонной книги"""
    if phonebook:
        print("Телефонная книга:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Телефонная книга пуста.")

def update_file():
    """Запись данных в файл"""
    with open("phonebook.txt", "w") as file:
        for name, phone in phonebook.items():
            file.write(f"{name}: {phone}\n")

def load_data_from_file():
    """Чтение данных из файла"""
    try:
        with open("phonebook.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, phone = line.strip().split(": ")
                phonebook[name] = phone
    except FileNotFoundError:
        pass  

# Загрузка данных из файла при запуске программы
load_data_from_file()

# Добавление одного контакта
print("Добавление контакта:")
name = input("Имя: ")
phone = input("Номер телефона: ")
add_contact(name, phone)

# Меню с функциями
while True:
    print("\nМеню:")
    print("1. Печать телефонной книги")
    print("2. Обновление номера телефона")
    print("3. Удаление контакта")
    print("4. Завершить")  
    
    choice = input("Выберите действие (1-4): ")

    if choice == '1':
        print_phonebook()
    elif choice == '2':
        name = input("Введите имя контакта для обновления номера: ")
        new_phone = input("Введите новый номер телефона: ")
        update_contact(name, new_phone)
    elif choice == '3':
        name = input("Введите имя контакта для удаления: ")
        delete_contact(name)
    elif choice == '4':
        break  
    else:
        print("Неверный ввод. Пожалуйста, введите число от 1 до 4.")