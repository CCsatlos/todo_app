list_todo = ['Homework', 'Shopping']


def show_menu():

    """It only prints the menu of the application"""

    print('Menu: \n')
    print('1. Show last ToDo')
    print('2. Add new ToDo.')
    print('3. Exit. \n')
    

def last_todo():
        
    """Print the last 'ToDo' from the list."""

    print(list_todo[-1])


def add_new_todo():
     
    """Add a new 'ToDo' to the list. 
            Parameters: 
                new_add (str): """

    new_add = input('Enter your new ToDo: ')
    list_todo.append(new_add)


def user_choice():
    """The function takes the input form keyboard.
        Parameter:
            choice (int): can be choose just 1, 2 or 3."""
    choice = int(input('Enter your choice and press ENTER: '))
    return choice



show_menu()

while True:
    choice = user_choice()  # Get the user's choice once
    if choice == 1:
        last_todo()
    elif choice == 2:
        add_new_todo()
    elif choice == 3:
        break  
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

 
    
        




        
   



     

