from utility import *
from colorama import Fore, init
from components import AddressBook
init(autoreset=True)

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input(f"Enter a command: {Fore.LIGHTCYAN_EX}")
        print(Fore.RESET, end="")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(', '.join(show_phone(args, book)))
        elif command == "all":
            print(colorize_message(f"{"Name":<20}{"Phone":<15}", "MAGENTA"))
            for i, contact in enumerate(show_all(book)):
                print(colorize_message(f"{contact.name:<20}{'\n                    '.join(contact.phones)}", f"{"CYAN" if i%2==0 else "BLUE"}"))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(colorize_message(f"{"Name":<20}{"Birthday":<15}", "MAGENTA"))
            for i, contact in enumerate(birthdays(book)):
                print(colorize_message(f"{contact.name:<20}{'\n                    '.join(contact.birthday)}", f"{"CYAN" if i%2==0 else "BLUE"}"))
        else:
            print(colorize_message("Invalid command.", "YELLOW"))

if __name__ == "__main__":
    main()
    # try:
    #     main()
    # except Exception as e:
    # # Обробка будь-якого винятку
    #     print(f"An error occurred: {e}")


# To start the project:
# python -m venv .venv

#   На Windows у командному рядку (CMD):
#       .\.venv\Scripts\activate.bat
#   На Windows у PowerShell:
#       .\.venv\Scripts\Activate.ps1
#   На macOS та Linux:
#       source .venv/bin/activate

# pip install -r requirements.txt

# To generate requirements.txt:
# pip freeze > requirements.txt

# To end:
#  deactivate