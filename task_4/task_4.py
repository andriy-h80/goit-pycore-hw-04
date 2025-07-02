
'''
Напишіть консольного бота помічника,
який розпізнаватиме команди, що вводяться з клавіатури,
та буде відповідати відповідно до введеної команди.
'''

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
    except:
        return "Format: add name phone"
    
    if not phone.isdigit():
        return "Phone must include only digit"

    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
        
    except:
        return "Format: change name phone"
    
    if not phone.isdigit():
        return "Phone must include only digit"
    
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return f"Контакт з іменем '{name}' не знайдено."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Контакт з іменем '{name}' не знайдено."

def show_all(contacts):
    if not contacts:
        return "Contacts list is empty"
    else:
        return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
    