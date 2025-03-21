from utility import parse_input, add_contact, change_contact, show_phone, show_all, colorize_message
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
            print(show_phone(args, book))
        elif command == "all":
            print(colorize_message(f"{"Name":<20}{"Phone":<15}", "MAGENTA"))
            for i, contact in enumerate(show_all(book)):
                print(colorize_message(f"{contact.name:<20}{contact.phone:<15}", f"{"CYAN" if i%2==0 else "BLUE"}"))
        else:
            print(colorize_message("Invalid command.", "YELLOW"))

if __name__ == "__main__":
    main()


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