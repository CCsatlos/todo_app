list_last_todo = []
choice = input('Enter your choice and press ENTER: ')


def show_menu():

    """It only prints the menu of the application"""

    print('Menu: \n')
    print('1. Show last ToDo')
    print('2. Add new ToDo.')
    print('3. Exit. \n')
    

def last_todo():
        
    """Print the last 'ToDo' from the list."""

    print(list_last_todo[-1])


def add_new_todo(new_add):
     
    """Add a new 'ToDo' to the list. 
            Parameters: 
                new_add (str): """

    new_add = input('Enter your new ToDo: ')
    return list_last_todo.append(new_add)

# while choice != 3:
#      if choice == 1:
#           last_todo()
#           show_menu()
#      elif choice == 2: 
#           add_new_todo(new_add)
#           show_menu()
#      else: 
#           print('ERROR')
#           show_menu()




     

