import common
import ui
import data_manager

title = '\nStudents'

list_labels = ['name',
                'age',
                'active']

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
            id = ui.get_inputs([''], 'ID: ')
            read_student(table, id)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    elif user_input == '6':
        pass
    elif user_input == '7':
        pass
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
            return student
    raise ValueError

def activate_deactivate_student(table, id):
    
    ACTIVE_DEACTIVE = 3

    for student in table:
        pass

















def delete_student(table, id):
    about_to_be_deleted = None
    ID = 0
    for row in table:
        if row[ID] == id:
            about_to_be_deleted = row
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




