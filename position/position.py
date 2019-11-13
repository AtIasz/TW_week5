import common
import ui
import data_manager
import main

title = '\nPosition'

list_labels = ['Description: ',
                'Number of Seats: ',
                'Company ID: ']

options = ['Create Position',
                'Read Position',
                'Read Positions',
                'Update Position',
                'Delete Position',
                'Back to Main Menu']
table = data_manager.get_table_from_file('position/position_data.csv')


def start_module():

    ui.print_menu(title, options, 'Exiting back to Main Menu...')
    user_input = ui.get_single_input("Your choice: ")
    if user_input == '1':
        create_Position(table)
    elif user_input == '2':
        try:
            id = ui.get_single_input("ID of the Position you are looking for:\n")
            read_Position(table, id)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '3':
        try:
            user_input = ui.get_single_input('How many Position would you like to search?\n')
            how_many = int(user_input)
            ids = ui.get_inputs(how_many*['ID: '], 'Positions ids')
            read_Positions(table, ids)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '4':
        try:
            id = ui.get_single_input("ID of the Position you are looking for:\n")
            update_Position(table, id)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '5':
        try:
            id = ui.get_single_input("ID of the Position you are looking for:\n")
            delete_Position(table, id)
        except ValueError:
            ui.print_error_message("Please enter a valid ID!")
    elif user_input == '6':
        main.main()


def show_table(table):

    ui.print_table(table)


def create_Position(table):
    '''
        Users can create new Positions. Positions have an ID, name, age, active.
        “active” determines if the Position is active or not (shows up in listings). 
        IDs are unique among Positions.
    '''
    ID = common.generate_random(table)
    user_input = ui.get_inputs(list_labels, title)
    user_input.insert(0, ID)

    table.append(user_input)

    return table


def read_Position(table, id):
    '''
    Users can show the details of existing Positions by entering their ID.
    All “Application” of Position shows up here.
    '''
    ID = 0
    for Position in table:
        if Position[ID] == id:
            ui.print_result('Position you were looking for', Position)
            return Position
    raise ValueError


def read_Positions(table, ids):
    # ids = list of ids, given by user

    final_list = []

    ID = 0
    for Position in table:
        for id in ids:
            if Position[ID] == id:
                final_list.append(Position)
    ui.print_result('Positions you were looking for', final_list)
    return final_list


def delete_Position(table, id):
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


def update_Position(table, id):
    
    ID = 0
    user_input = ui.get_inputs(list_labels, title)

    for n, row in enumerate(table):
        if id == row[ID]:
            user_input.insert(0, id)
            change = user_input
            table[n] = change

    table = data_manager.write_table_to_file(table)

    return table
