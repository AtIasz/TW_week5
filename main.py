import ui
import sys
import students
import data_manager

def choose():
    table = data_manager.get_data_from_file()
    user_input = int(input("Please type a number!\n"))
    if user_input == 1:
        students.create_student(table)
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        try:
            id = input("Give me the ID of the student: \n")
            students.update_student(table, id)
        except ValueError:
            ui.print_error_message("Wrong input!")
    elif user_input == 5:
        pass
    elif user_input == 6:
        try:
            id = input("Give me the ID of the student: \n")
            students.delete_student(table, id)
        except ValueError:
            ui.print_error_message("Wrong input!")
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