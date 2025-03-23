from colorama import Fore, init
from collections import namedtuple
from components import AddressBook, Record, Birthday, Phone, Name


init(autoreset=True)
COLORS_SET={
        'BLUE'        :Fore.BLUE,
        'GREEN'       :Fore.GREEN,
        'YELLOW'      :Fore.YELLOW,
        'RED'         :Fore.RED,
        'MAGENTA'     :Fore.MAGENTA,
        'CYAN'        :Fore.CYAN,
        'LIGHTCYAN_EX':Fore.LIGHTCYAN_EX,
    }

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return colorize_message("Give me name and  phone please.", "RED")
        except KeyError:
            return colorize_message("Give me name and phone please.", "RED")
        except IndexError:
            return colorize_message("Enter user name.", "RED")
    return inner

def colorize_message(message, color):
    color=color.upper()
    if color in COLORS_SET.keys():
        return f"{COLORS_SET[color]}{message}{Fore.RESET}"
    else:
        return f"{Fore.WHITE}{message}{Fore.RESET}"
    
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return colorize_message(message, "GREEN")

@input_error
def change_contact(args, book: AddressBook):
    name, phone, new_phone, *_ = args
    record = book.find(name)
    record.edit_phone(phone, new_phone)
    message = "Contact updated."
    return colorize_message(message, "GREEN")


@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    return record.get_phones

def show_all(book: AddressBook):
    list_of_contacts = []
    Contact = namedtuple('Contact', ['name', 'phones'])
    for name, record in book.get_all_records.items():
        list_of_contacts.append(Contact(name, record.get_phones))
    return sorted(list_of_contacts)

@input_error
def add_birthday(args, book: AddressBook):
    name, birthay, *_ = args
    record = book.find(name)
    record.add_birthday(birthay)
    message = "Contact updated."
    return colorize_message(message, "GREEN")

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    print(record)
    res = record.get_birthday
    return res if res else 'Birthday not added yet.'

def birthdays(book: AddressBook):
    print(book.get_upcoming_birthdays())
    return book.get_upcoming_birthdays()

if __name__ == "__main__":
    pass
