list_todo = ['Homework', 'Shopping']

def last_todo():
        
    """Print the last 'ToDo' from the list."""

    print(list_todo[-1])

def add_new_todo():
     
    """Add a new 'ToDo' to the list. 
            Parameters: 
                new_add (str): """

    new_add = input('Enter your new ToDo: ')
    list_todo.append(new_add)

command_list = {
    1 : {'title' : 'Show last ToDo', 'command' : last_todo},
    2 : {'title' : 'Add new ToDo', 'command' : add_new_todo},
    # 3 : {'title' : 'Modify ToDo`s', 'command' : functie}
    }

def main_menu_with_input (cl):
    for k, v in cl.items():
        print(k, v['title'])
    user_choice = int(input('Please enter a number and press ENTER: '))

    exe_command = cl.get(user_choice)

    if exe_command:
        exe_command['command']()
    else:
        print('Invalid choice')

main_menu_with_input(command_list)