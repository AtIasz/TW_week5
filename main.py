import ui
import sys
from students import students
import data_manager
from company import company
from position import position
from application import application


def choose():
    user_input = ui.get_single_input("Please type a number!\n")
    if user_input == '1':
        application.start_module()
    elif user_input == '2':
        company.start_module()
    elif user_input == '3':
        position.start_module()
    elif user_input == '4':
        students.start_module()
    #elif user_input == '5':
    #    gen()

    elif user_input == '0':
        sys.exit()
    else:
        raise KeyError("There is no such option!")

def handle_menu():
    options = ['Application Manager',
                'Company Manager',
                'Position Manager',
                'Students Manager']

    ui.print_menu('Main Menu', options, "Exit")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError:
            ui.print_error_message('Wrong input! Please try again!')
def gen():
    lmao=[]
    for i in range(10):
        eksz=data_manager.ID_gen()
        lmao.append(eksz)
    with open("company/company_data.csv","a") as f:
            for i in range(len(lmao)):
                f.write(lmao[i]+"\n")
             





















if __name__ == "__main__":
    main()