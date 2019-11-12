import common
import data_manager
import ui

title = 'Company'
list_labels = ['Company name: ']

options = ['Create Company',
            'Read Company',
            'Read Companies',
            'Update Company',
            'Delete Company',
            'Back to Main Menu']

exit_message = "Return to Main Menu..."

def start_module():
    ui.print_menu(title, options, exit_message)


def create_company(table):
    ID = common.generate_random(table)
    user_input = ui.get_inputs(list_labels, title)
    user_input.insert(0, ID)
    table.append(user_input)
    return table



def read_company():
    pass
def read_companies():
    pass
def update_company():
    pass
def delete_company():
    pass
