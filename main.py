# {("first_name", "last_name"): ("phone_number", "sity", "state")  }
phonebook = {}

def add_entry():
    try:
        first_name = input("Enter first name: ").strip().capitalize()
        last_name = input("Enter last name: ").strip().capitalize()
        phone_number = input("Enter phone number: ").strip().capitalize()
        city = input("Enter city: ").strip().capitalize()
        state = input("Enter state: ").strip().upper()

        if not all([first_name, last_name, phone_number, city, state]):
            print("Error: All fields are required!")
            return False

        if (first_name, last_name) in phonebook:
            print("Error: This person is already in the phonebook!")
            return False

        phonebook[(first_name, last_name)] = (phone_number, city, state)
        print(f"\n {first_name} {last_name} added to the phonebook!")
        return True
        
    except Exception as e:
        print(f"Error adding entry: {str(e)}")
        return False

def search_by_first_name():
    found = False
    name_to_search = input("Enter first name: ").lower()
    for (first_name, last_name), (phone_number, city, state) in phonebook.items():
        if first_name.lower() == name_to_search:
            print(f'Found person: {first_name} {last_name}, phone number: {phone_number}, city: {city}, state: {state}')
            found = True
    if not found:
        print("A person by that name has not been found")

def search_by_last_name(): # Андрій
    results = []

    l_name = input("Enter last name: ").strip()

    for (first_name, last_name), (phone_number, city, state) in phonebook.items():
        if last_name.lower() == l_name.lower():
            results.append((first_name, last_name, phone_number, city, state))
            found = True
    print(f"Found entries: {results}") if results else print(f"No entries found for entered last name '{l_name}'.")

    # return results

def search_by_full_name():
    while True:
        full_name = input("\nEnter full name or type 'back' to return to Phonebook Menu: ").strip()

        if full_name.lower() == "back":
            return

        if " " not in full_name:
            print("Please enter both first and last name separated by space.")
            continue

        first_name, last_name = full_name.split(" ", 1)
        found = False
        for (fn, ln), (phone, city, state) in phonebook.items():
            if fn.lower() == first_name.lower() and ln.lower() == last_name.lower():
                print(f"\nFound contact:")
                print(f"Name: {fn} {ln}")
                print(f"Phone number: {phone}")
                print(f"City: {city}")
                print(f"State: {state}")
                found = True
                break

        if not found:
            print("No matching contact found.")

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

def search_by_city_or_state(): # Ростислав
    query = input("Enter city or state to search: ").strip().lower()
    results = []
    for (first_name, last_name), (phone_number, city, state) in phonebook.items():
        if query == city.lower() or query == state.lower():
            results.append(f"{first_name} {last_name}: {phone_number}, {city}, {state}")
    if results:
        print("\n".join(results))
    else:
        print("No entries found for the given city or state.")

def delete_by_phone_number(): # Дмитро
    print("Delete a record by telephone number")
    phonebook = {("Dmytro", "Shostak"): ("+380991234567", "Kyiv", "Ukraine")}
    print("Current phonebook:", phonebook)
    for key, value in list(phonebook.items()):
        if value[0] == phone:
            del phonebook[key]
            print(f"Record with phone number {phone} deleted.")
            break
    else:
        print("Phone number not found.")

    print("Updated phonebook:", phonebook)
    return phonebook

def update_by_phone_number(phone_number, new_person): # Юлія
    print("Update a record by telephone number - stub")

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
    application_loop()

main()
search_by_phone_number()