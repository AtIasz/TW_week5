import ui
import sys
from students import students
import data_manager
from company import company
from position import position
from application import application

def choose():
    user_input = int(input("Please type a number!\n"))
    if user_input == 1:
        pass
    elif user_input == 2:
        company.start_module()
    elif user_input == 3:
        pass
    elif user_input == 4:
        students.start_module()
    elif user_input == 5:
        pass
    elif user_input == 6:
        pass
    elif user_input == 0:
        pass # MAIN MENU go back to main menu
    else:
        raise KeyError("There is no such option!")

def handle_menu():
    options = ['Application Manager',
                'Company Manager',
                'Position Manager',
                'Students Manager']

    ui.print_menu('Main Menu', options, 'Exit program')


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError:
            ui.print_error_message('Wrong input! Please try again!')





















if __name__ == "__main__":
    main()