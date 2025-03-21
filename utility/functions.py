from colorama import Fore, init
from collections import namedtuple

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
            return colorize_message("Give me name and phone please.", "RED")
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
def add_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        return colorize_message("Contact has already been added to the phonebook. You can try another name.", "YELLOW")
    contacts[name] = phone
    return colorize_message("Contact added.", "GREEN")

@input_error
def change_contact(args, contacts):
    name, phone = args
    if not name in contacts.keys():
        contacts[name] = phone
        return colorize_message("The contact was not found in the phone book so we added it.", "GREEN")
    contacts[name] = phone
    return colorize_message("Contact updated.", "GREEN")

@input_error
def show_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    if phone is None:
        return colorize_message(f"No contact {name} in the phonebook.", "GREEN")
    return phone


def show_all(contacts):
    list_of_contacts = []
    Contact = namedtuple('Contact', ['name', 'phone'])
    for key, value in contacts.items():
        list_of_contacts.append(Contact(key, value))
    return sorted(list_of_contacts)

if __name__ == "__main__":
    pass
