import common
import ui
import data_manager
import main

title = '\nStudents'

list_labels = ['Name: ',
                'Age: ',
                'Active (1) = Yes, (0) = No: ']

options = ['Create Student',
                'Read Student',
                'Read Students',
                'Update Student',
                'Activate/Deactivate Student',
                'Delete Student',
                'Back to Main Menu']
table = data_manager.get_table_from_file('students/students_data.csv')


def start_module():

    ui.print_menu(title, options, 'Exiting back to Main Menu...')
    user_input = ui.get_single_input("Your choice: ")
    if user_input == '1':
        create_student(table)
    elif user_input == '2':
        try:
            id = ui.get_single_input("ID of the student you are looking for:\n")
            read_student(table, id)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '3':
        try:
            user_input = ui.get_single_input('How many student would you like to search?\n')
            how_many = int(user_input)
            ids = ui.get_inputs(how_many*['ID: '], 'Students ids')
            read_students(table, ids)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '4':
        try:
            id = ui.get_single_input("ID of the student you are looking for:\n")
            update_student(table, id)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '5':
        try:
            id = ui.get_single_input("ID of the student you are looking for:\n")
            activate_deactivate_student(table, id)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '6':
        try:
            id = ui.get_single_input("ID of the student you are looking for:\n")
            delete_student(table, id)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '7':
        main.main()


def show_table(table):

    ui.print_table(table)


def create_student(table):
    '''
        Users can create new students. Students have an ID, name, age, active.
        “active” determines if the student is active or not (shows up in listings). 
        IDs are unique among students.
    '''
    ID = common.generate_random(table)
    user_input = ui.get_inputs(list_labels, title)
    user_input.insert(0, ID)

    table.append(user_input)

    return table


def read_student(table, id):
    '''
    Users can show the details of existing students by entering their ID.
    All “Application” of student shows up here.
    '''
    ID = 0
    for student in table:
        if student[ID] == id:
            ui.print_result('Student you were looking for', student)
            return student
    raise ValueError


def read_students(table, ids):
    # ids = list of ids, given by user

    final_list = []

    ID = 0
    for student in table:
        for id in ids:
            if student[ID] == id:
                final_list.append(student)
    ui.print_result('Students you were looking for', final_list)
    return final_list


def activate_deactivate_student(table, id):
    ID = 0
    ACTIVE_DEACTIVE = 3

    user_input = ui.get_single_input('Would you like to Activate (A) or Deactivate (D) the student?\n')

    for student in table:
        if student[ID] == id:
            if user_input == 'a' or user_input == 'A':
                student[ACTIVE_DEACTIVE] = 1
            elif user_input == 'd' or user_input == 'D':
                student[ACTIVE_DEACTIVE] = 0
            else:
                raise ValueError('Invalid input!')
    return table


def delete_student(table, id):
    about_to_be_deleted = None
    ID = 0
    for row in table:
        if row[ID] == id:
            about_to_be_deleted = row
            break
    if about_to_be_deleted is None:
        ui.print_error_message("Wrong input! Please try again!")
    else:
        table.remove(about_to_be_deleted)

    return table


def update_student(table, id):
    
    ID = 0
    user_input = ui.get_inputs(list_labels, title)

    for n, row in enumerate(table):
        if id == row[ID]:
            user_input.insert(0, id)
            change = user_input
            table[n] = change

    table = data_manager.write_table_to_file(table)

    return table

'''
def handle_menu():
    
    ui.print_menu('Main Menu', options)


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError:
            ui.print_error_message('Wrong input! Please try again!')
'''


