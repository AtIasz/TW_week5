def print_menu(title, options, exit_message):
    print(title)
    for i in range(len(options)):
        print('(' + str(i+1) + ')', end='')
        print(options[i])


def print_something_else(arg):
    pass

def get_inputs(arg):
    pass

def print_error_message(message):
    print(message)


def get_inputs(list_labels, title):

    print(title)
    user_inputs = []
    for i in list_labels:
        user_inputs.append(input(i))

    return user_inputs


def print_table(table, title_list):

    print(title_list)
    for item in table:
        print(item)

