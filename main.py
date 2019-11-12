import ui
import sys

def choose():
    user_input = int(input("Please type a number!\n"))
    if user_input == 1:
        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    elif user_input == 5:
        pass
    elif user_input == 6:
        pass
    elif user_input == 0:
        sys.exit(0)
    else:
        raise KeyError("There is no such option!")

def handle_menu():
    options = ['Create Student',
                'Read Student',
                'Read Students',
                'Update Student',
                'Activate/Deactivate Student',
                'Delete Student']
    ui.print_menu('Main Menu', options)


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError:
            ui.print_error_message('Wrong input! Please try again!')





















if __name__ == "__main__":
    main()