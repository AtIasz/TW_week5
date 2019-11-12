import common
import ui
import data_manager

title = 'Students'

list_labels = ['name',
                'age',
                'active']

options = ['Create Student',
                'Read Student',
                'Read Students',
                'Update Student',
                'Activate/Deactivate Student',
                'Delete Student']

def start_module():

    ui.print_menu(title, options)

def show_table(table):

   #ui.print


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




