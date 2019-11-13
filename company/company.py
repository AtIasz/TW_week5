import common
import data_manager
import ui

title = 'Company'
list_labels = ['Company name: ']



exit_message = "Return to Main Menu..."

def start_module():
    while True:
        handle_menu()
        try:
            choose()
        except ValueError as e:
            print(e)
    

def create_company(table):
    ID = common.generate_random(table)
    user_input = ui.get_inputs(list_labels, title)
    user_input.insert(0, ID)
    table.append(user_input)
    return table

def choose():
    ch=ui.get_inputs()
    list_of_companies=data_manager.get_data_from_file()
    if ch=="1":
        create_company(list_of_companies)
    elif ch=="2":
        read_company()
    elif ch=="3":
        read_companies()
    elif ch=="4":
        update_company()
    elif ch=="5":
        delete_company()
def read_company():
    pass
def read_companies():
    pass
def update_company():
    pass
def delete_company():
    pass

def handle_menu():
    pass
    options = ['Create Company',
                'Read Company',
                'Read Companies',
                'Update Company',
                'Delete Company',
                'Back to Main Menu']
    ui.print_menu(title, options, exit_message)
