from tkinter import ttk
from tkinter import Tk, Frame, Label, Button, LabelFrame, Toplevel, Entry

#creating the root
root = Tk()
root.title("Task Management")
root.config(bg = "white")
root.resizable(0, 0)

#establishing function for employees list
def employee_window():
    new_window = Toplevel(add_del_button)
    new_window.title("Employee window")
    new_window.geometry("450x200+160+120")

    name = Label(new_window, text = "First and last name").grid(column = 0, row = 0, padx = 10, pady = 10)
    hour = Label(new_window, text = "Working hours per day").grid(column = 0, row = 1, padx = 10, pady = 10)
    first_name_entry = Entry(new_window).grid(column = 1, row = 0, padx = 10, pady = 10)
    second_name_entry = Entry(new_window).grid(column = 2, row = 0, padx = 10, pady = 10)
    hours_entry = Entry(new_window).grid(column = 1, row = 1, padx = 10, pady = 10)
    save_button = Button(new_window, text = "Save").grid(column = 1, row = 2, ipadx = 10, pady=10)

#creating the two main frames for interface
left_frame = Frame(root, name = "left frame")
left_frame.grid(column = 0, row = 0)
right_frame = Frame(root, name="right frame")
right_frame.grid(column = 1, row = 0, sticky = "n")

#setting the left frame
employees_label = LabelFrame(left_frame, text = "Employees")
employees_label.grid(column = 0, row = 0, padx = 20, pady = 20)
all_emp_button = Button(employees_label, text = "Select all employees").grid(column = 0, row = 0)
select_button = Button(employees_label, text = "Select the employees").grid(column = 0, row = 1)
add_del_button = Button(employees_label, text = "Delete/delete an employee", command=employee_window).grid(column = 0, row = 2)

#setting the position of all available widgets into the left frame
for button in employees_label.winfo_children():
    button.grid_configure(padx = 20, pady = 10, sticky = "ew")

#setting the second/right frame
task_label = LabelFrame(left_frame, text = "Tasks")
task_label.grid(column = 0, row = 1, padx = 20, pady = 20)
add_task_button = Button(task_label, text = "Import the tasks").grid(column = 0, row = 0)
man_task_button = Button(task_label, text = "Add a task manually").grid(column = 0, row = 1)
del_task_button = Button(task_label, text = "Delete a task").grid(column = 0, row = 2)

#setting the position of all available widgets into the left frame
for button in task_label.winfo_children():
    button.grid_configure(padx = 20, pady = 10, sticky = "ew")

#continuing with labels frame
data_int_label = LabelFrame(left_frame, text = "Data logs")
data_int_label.grid(column = 0, row = 2, padx = 20, pady = 20)
logs_label = Label(data_int_label, text = "Should be display the last few logs").grid(column = 0, row = 0, padx=10, pady=10)

#setting the right frame
planning = LabelFrame(right_frame, text="Planning")
planning.grid(column = 0, row = 0, padx = 20, pady = 20)

#creating the labels for the right frame
month_label = Label(planning, text = "Month/Day")
hour = Label(planning, text = "Hour")
task_name = Label(planning, text = "Task name")
name = Label(planning, text = "Employee")
target_date = Label(planning, text = "Target date")

#setting the geometry of all available widgets into the right children frame
w_colum = 0

for widget in planning.winfo_children():
    widget.grid(column = w_colum, row = 0)
    w_colum += w_colum + 1

#positioning the labels into the right right frame
for widget in planning.winfo_children():
    widget.grid(padx=50)
    
root.mainloop()