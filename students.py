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














