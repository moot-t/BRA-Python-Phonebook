import json
import os

# Ім'я файлу для збереження даних
pb_file = "phonebook.json"
phonebook = {}

def save_phonebook():
    try:
        serializable_phonebook = {
            f"{first_name},{last_name}": [phone_number, city, state]
            for (first_name, last_name), (phone_number, city, state) in phonebook.items()
        }

        with open(pb_file, 'w', encoding='utf-8') as file:
            json.dump(serializable_phonebook, file, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"\nError saving phonebook: {str(e)}")
        return False

def load_phonebook():
    global phonebook
    if os.path.exists(pb_file):
        with open(pb_file, 'r') as file:
            data = json.load(file)
            # Конвертуємо назад у кортежі
            phonebook = {
                tuple(key.split(',')): tuple(value)
                for key, value in data.items()
            }
    return True


def add_entry():
    try:
        first_name = input("Enter first name: ").strip().capitalize()
        last_name = input("Enter last name: ").strip().capitalize()
        phone_number = input("Enter phone number: ").strip()
        city = input("Enter city: ").strip().capitalize()
        state = input("Enter state: ").strip().upper()

        if not all([first_name, last_name, phone_number, city, state]):
            print("Error: All fields are required!")
            return False

        # Перевірка на існуючий номер телефону
        for _, (existing_phone, _, _) in phonebook.items():
            if existing_phone == phone_number:
                print("\nError: This phone number already exists in the phonebook!")
                return False

        # Перевірка на існування контакту з таким іменем та прізвищем
        for (f_name, l_name), _ in phonebook.items():
            if f_name.lower() == first_name.lower() and l_name.lower() == last_name.lower():
                print("\nError: Contact with this first name and last name already exists!")
                return False

        phonebook[(first_name, last_name)] = (phone_number, city, state)
        print(f"\n {first_name} {last_name} added to the phonebook!")
        save_phonebook()  # Зберігаємо після додавання
        return True

    except Exception as e:
        print(f"Error adding entry: {str(e)}")
        return False

def search_by_name(search_type='first'):
    found = False
    if search_type == 'full':
        first_name = input("Enter first name: ").strip().lower()
        last_name = input("Enter last name: ").strip().lower()
        
        for (f_name, l_name), (phone_number, city, state) in phonebook.items():
            if f_name.lower() == first_name and l_name.lower() == last_name:
                print(f'\nFound person: {f_name} {l_name}, phone number: {phone_number}, city: {city}, state: {state}')
                found = True
        
        if not found:
            print(f"\nNo entries found for {first_name.capitalize()} {last_name.capitalize()}")
    else:
        name_type = "first name" if search_type == 'first' else "last name"
        name_to_search = input(f"Enter {name_type}: ").strip().lower()
        
        for (first_name, last_name), (phone_number, city, state) in phonebook.items():
            current_name = first_name.lower() if search_type == 'first' else last_name.lower()
            if current_name == name_to_search:
                print(f'\nFound person: {first_name} {last_name}, phone number: {phone_number}, city: {city}, state: {state}')
                found = True
        
        if not found:
            print(f"\nNo entries found for entered {name_type} '{name_to_search}'.")

def search_by_first_name():
    search_by_name('first')

def search_by_last_name():
    search_by_name('last')

def search_by_full_name():
    search_by_name('full')

def search_by_phone_number():
    phone = input("Enter the phone number to search: ")
    found = False
    for (first_name, last_name), (phone_number, city, state) in phonebook.items():
        if phone_number == phone:
            print(f"Found: {first_name} {last_name} | Phone: {phone_number} | City: {city} | State: {state}")
            found = True
            break
    if not found:
        print("No entry found with that phone number.")

def search_by_city_or_state():
    query = input("Enter city or state to search: ").strip().lower()
    results = []
    for (first_name, last_name), (phone_number, city, state) in phonebook.items():
        if query == city.lower() or query == state.lower():
            results.append(f"{first_name} {last_name}: {phone_number}, {city}, {state}")
    if results:
        print("\n".join(results))
    else:
        print("No entries found for the given city or state.")

def delete_by_phone_number():
    try:
        phone_to_delete = input("Enter phone number to delete: ").strip()
        
        for key, value in list(phonebook.items()):
            if value[0] == phone_to_delete:
                del phonebook[key]
                print(f"\nRecord with phone number {phone_to_delete} deleted.")
                save_phonebook()  # Зберігаємо після видалення
                return True
        
        print(f"\nNo entry found with phone number {phone_to_delete}")
        return False
        
    except Exception as e:
        print(f"\nError deleting entry: {str(e)}")
        return False

def update_by_phone_number():
    try:
        phone_to_update = input("Enter phone number to update: ").strip()
        
        found = False
        for (first, last), (phone, city, state) in phonebook.items():
            if phone == phone_to_update:
                found = True
                new_phone = input("Enter new phone number (or press Enter to keep current): ").strip()
                new_city = input("Enter new city (or press Enter to keep current): ").strip().capitalize()
                new_state = input("Enter new state (or press Enter to keep current): ").strip().upper()
                
                # Якщо користувач не ввів нове значення, залишаємо старе
                if not new_phone:
                    new_phone = phone
                if not new_city:
                    new_city = city
                if not new_state:
                    new_state = state
                
                phonebook[(first, last)] = (new_phone, new_city, new_state)
                print(f"\nUpdated entry for {first} {last}")
                save_phonebook()  # Зберігаємо після оновлення
                return True
            if phone_to_update in [contact['phone_number'] for contact in phonebook]:
                print("Error: This phone number already exists in the phonebook")
                return False

        if not found:
            print(f"\nNo entry found with phone number {phone_to_update}")
            return False
            
    except Exception as e:
        print(f"\nError updating entry: {str(e)}")
        return False

def exit_program():
    print("Exiting program.")
    return False

def application_loop():
    is_working = True
    while is_working:
        print("""\nPhonebook Menu:
1) Add new entries 
2) Search by first name 
3) Search by last name 
4) Search by full name
5) Search by telephone number
6) Search by city or state
7) Delete a record for a given telephone number
8) Update a record for a given telephone number
9) Exit the program""")
        try:
            choice = int(input('Your choice: '))
        except ValueError:
            print("Please enter a valid number from 1 to 9.")
            continue

        match choice:
            case 1:
                add_entry()
            case 2:
                search_by_first_name()
            case 3:
                search_by_last_name()
            case 4:
                search_by_full_name()
            case 5:
                search_by_phone_number()
            case 6:
                search_by_city_or_state()
            case 7:
                delete_by_phone_number()
            case 8:
                update_by_phone_number()
            case 9:
                is_working = exit_program()
            case _:
                print("Invalid choice. Please select a number from 1 to 9.")

def main():
    try:
        load_phonebook()
        application_loop()
        save_phonebook()
    except KeyboardInterrupt:
        print("\n...Exiting program")
main()