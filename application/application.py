import common
import ui
import data_manager
import main

title = '\nApplication'

list_labels = ['Description: ',
                'Number of Seats: ',
                'Company ID: ']

options = ['Create Application',
                'Update Application',
                'Delete Application',
                'Back to Main Menu']
table = data_manager.get_table_from_file('application/application_data.csv')


def start_module():

    ui.print_menu(title, options, 'Exiting back to Main Menu...')
    user_input = ui.get_single_input("Your choice: ")
    if user_input == '1':
        create_Application(table)
    elif user_input == '2':
        try:
            id = ui.get_single_input("ID of the Application you are looking for:\n")
            update_Application(table, id)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '3':
        try:
            id = ui.get_single_input("ID of the Application you are looking for:\n")
            delete_Application(table, id)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '4':
        main.main()


def show_table(table):

    ui.print_table(table)


def create_Application(table):
    '''
        Users can create new Applications. Applications have an ID, name, age, active.
        “active” determines if the Application is active or not (shows up in listings). 
        IDs are unique among Applications.
    '''
    ID = common.generate_random(table)
    user_input = ui.get_inputs(list_labels, title)
    user_input.insert(0, ID)

    table.append(user_input)
    new_table = data_manager.write_table_to_file('application_data.csv', table)
    return new_table


def delete_Application(table, id):
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


def update_Application(table, id):
    
    ID = 0
    user_input = ui.get_inputs(list_labels, title)

    for n, row in enumerate(table):
        if id == row[ID]:
            user_input.insert(0, id)
            change = user_input
            table[n] = change

    table = data_manager.write_table_to_file(table)

    ui.print_menu(title, options, exit_message)
