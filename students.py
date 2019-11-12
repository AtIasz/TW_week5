import common
import ui

title = 'Students'

list_labels = ['ID',
                'name',
                'age',
                'active']


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


def read_student(ID="!hZK87%u"):
    '''
    Users can show the details of existing students by entering their ID.
    All “Application” of student shows up here.
    '''
    data=data_manager.get_data_from_file()
    for i in range(len(data)):
        if data[i][0]==ID:
            return data[i]
    raise ValueError


















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
