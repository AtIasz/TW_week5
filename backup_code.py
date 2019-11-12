table = data_manager.get_data_from_file()
user_input = int(input("Please type a number!\n"))
if user_input == 1:
    students.create_student(table)
elif user_input == 2:
    pass
elif user_input == 3:
    pass
elif user_input == 4:
    try:
        id = input("Give me the ID of the student: \n")
        students.update_student(table, id)
    except ValueError:
        ui.print_error_message("Wrong input!")
elif user_input == 5:
    pass
elif user_input == 6:
    try:
        id = input("Give me the ID of the student: \n")
        students.delete_student(table, id)
    except ValueError:
        ui.print_error_message("Wrong input!")
elif user_input == 0:
    pass # MAIN MENU go back to main menu
else:
    raise KeyError("There is no such option!")





