def print_menu(title, options):
    print(title)
    
    for i in range(len(options)):
        print('(' + str(i+1) + ')', end='')
        print(options[i])
        
    print("(0)Exit")

def print_something_else(arg):
    pass

def get_inputs():
    data_in=input()

def print_error_message(message):
    print(message)


def get_inputs(list_labels, title):

    print(title)
    user_inputs = []
    for i in list_labels:
        user_inputs.append(input(i))

    return user_inputs


def get_single_input(message_to_user):
    
    user_input = input(message_to_user)
    
    return user_input

def print_table(table, title_list):


    pass