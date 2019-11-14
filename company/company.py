import common
import data_manager
import ui
import position

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
    

def create_company(list_of_data):
    """
    Users can create new companies. Companies have an ID, name.
    IDs and names of companies are unique amongst other companies.

    """
    ID = common.generate_random(list_of_data)
    user_input = ui.get_inputs(list_labels, title)
    user_input.insert(0, ID)
    list_of_data.append(user_input)
    return list_of_data

def choose():
    ch=input("Give me a number: ")
<<<<<<< HEAD
    list_of_companies=data_manager.get_data_from_file(filename="company/company_data.csv")
    if ch == "1":
=======
    list_of_companies = data_manager.get_data_from_file(filename="company/company_data.csv")
    if ch=="1":
>>>>>>> 65d8add016f3059dec1bf880b8539f93233a23ad
        create_company(list_of_companies)
    elif ch == "2":
        ui.print_something(read_company("SALALALA"))
    elif ch == "3":
        read_companies(list_of_companies)
    elif ch == "4":
        update_company()
    elif ch == "5":
        delete_company()
    
        
        
        
def read_company(ID):
    """
    Users can show the details of existing companies by entering their ID.
    All “Position” of a company shows up here.

    """
    pass
    list_of_company_positions= data_manager.get_data_from_file(filename="position/position_data.csv")
    for i in range(len(list_of_company_positions)):
    



def read_companies(list_of_companies):
    """ 
    Users can list the IDs and names of all companies in the system.
    
    """
    list_of_companies_data = data_manager.get_data_from_file(filename="company/company_data.csv")
    
    ui.print_something(list_of_companies)
    pass

def update_company(ID):
    """
    Users can update the details of existing companies by first entering their ID and then the information (name) to be updated.
    IDs cannot be updated.
    Company names can be updated, but they should stay unique.

    """
    list_of_companies = data_manager.get_data_from_file(filename="position/position.csv")
    for i in range(len(list_of_companies)):
        if list_of_companies[i][0] == ID:
            pass
def delete_company():
    pass
    """
    Users can delete existing companies by entering their ID.
    Companies cannot be deleted if they have an existing “Position”.
    """
    

def handle_menu():
    pass
    options = ['Create Company',
                'Read Company',
                'Read Companies',
                'Update Company',
                'Delete Company',]
    ui.print_menu(title, options, exit_message)
