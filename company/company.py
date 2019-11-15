import common
import data_manager
import ui
import position
import main

title = 'Company'
list_labels = ['Company name: ']



exit_message = "Return to Main Menu..."

def start_module():
    while True:
        handle_menu()
        try:
            choose()
        except ValueError:
            ui.print_error_message("Please choose a valid option!")
    


def choose():
    ch=input("Give me a number: ")
    list_of_companies = data_manager.get_data_from_file(filename="company/company_data.csv")
    if ch=="1":
        create_company(list_of_companies)
    elif ch == "2":
        x=input("Give me an ID I can work with: ")
        ui.print_something(read_company(x))
    elif ch == "3":
        ui.print_something(read_companies())
    elif ch == "4":
        x=input("Give me an ID I can work with: ")
        update_company(x)
    elif ch == "5":
        x=input("Give me an ID I can work with: ")
        delete_company(x)
    elif ch == '0':
        main.main()
        
def create_company(list_of_data):
    """
    Users can create new companies. Companies have an ID, name.
    IDs and names of companies are unique amongst other companies.

    """
    ID = common.generate_random(list_of_data)
    user_input = ui.get_inputs(list_labels, title)
    user_input.insert(0, ID)
    list_of_data.append(user_input)
    with open("company/company_data.csv","w") as f:
            for i in range(len(list_of_data)):
                row = ','.join(list_of_data[i])
                f.write(row + '\n')
    
    
        
        
def read_company(ID):
    """
    Users can show the details of existing companies by entering their ID.
    All “Position” of a company shows up here.

    """
    pass
    return_list=[]
    list_of_company_positions = data_manager.get_data_from_file(filename = "position/position_data.csv")
    for i in range(len(list_of_company_positions)):
        if list_of_company_positions[i][-1] == ID:
            return_list.append(list_of_company_positions[i])
    return return_list

def read_companies():
    """ 
    Users can list the IDs and names of all companies in the system.
    
    """
    list_of_companies = data_manager.get_data_from_file(filename="company/company_data.csv")
    return list_of_companies
    

 
def update_company(ID):
    """
    Users can update the details of existing companies by first entering their ID and then the information (name) to be updated.
    IDs cannot be updated.
    Company names can be updated, but they should stay unique.

    """
    list_of_companies = data_manager.get_data_from_file(filename="company/company_data.csv")
    exist = False
    return_list=[]
    place_of_new_name = 0
    for i in range(len(list_of_companies)):
        if ID == list_of_companies[i][0]:
            exist = True
            place_of_new_name = i
    if exist != True:
        return "No company is in the database with such ID"
    else:
        x = input("Give me this specific ID a new company name:")
        tmp=[]
        tmp.append(list_of_companies[place_of_new_name][0])
        tmp.append(x)
        for i in range(len(list_of_companies)):
            if i == place_of_new_name:
                return_list.append(tmp)
            else:
                return_list.append(list_of_companies[i])
        with open("company/company_data.csv","w") as f:
            for i in range(len(return_list)):
                row = ','.join(return_list[i])
                f.write(row + '\n')

def delete_company(ID):
    pass
    """
    Users can delete existing companies by entering their ID.
    Companies cannot be deleted if they have an existing “Position”.
    """
    list_of_companies = data_manager.get_data_from_file(filename="company/company_data.csv")
    list_of_company_positions = data_manager.get_data_from_file(filename = "position/position_data.csv")

    theres = False
    for i in range(len(list_of_company_positions)):
        if list_of_company_positions[i][-1] == ID:
            return "This company has positions, so it can't be deleted."       
    return_list = []
    for i in range(len(list_of_companies)):
        if list_of_companies[i][0] != ID:
            return_list.append(list_of_companies[i])
    
    with open("company/company_data.csv", "w") as f:
        for i in range(len(return_list)):
            row = ','.join(return_list[i])
            f.write(row + '\n')            

def handle_menu():
    pass
    options = ['Create Company',
                'Read Company',
                'Read Companies',
                'Update Company',
                'Delete Company',]
    ui.print_menu(title, options, exit_message)
