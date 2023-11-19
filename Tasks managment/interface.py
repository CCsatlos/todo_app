from tkinter import ttk
from tkinter import Tk, Frame, Label, Button, LabelFrame

root = Tk()
root.title("Task Management")
root.config(bg = "white")
root.resizable(1, 1)

left_frame = Frame(root, name = "left frame")
left_frame.grid(column = 0, row = 0)
right_frame = Frame(root, name="right frame")
right_frame.grid(column = 1, row = 0, sticky = "n")

employees_label = LabelFrame(left_frame, text = "Employees")
employees_label.grid(column = 0, row = 0, padx = 20, pady = 20)
all_emp_button = Button(employees_label, text = "Select all employees").grid(column = 0, row = 0)
select_button = Button(employees_label, text = "Select the employees").grid(column = 0, row = 1)
delete_button = Button(employees_label, text = "Delete an employee").grid(column = 0, row = 2)

for button in employees_label.winfo_children():
    button.grid_configure(padx = 20, pady = 10, sticky = "ew")

task_label = LabelFrame(left_frame, text = "Tasks")
task_label.grid(column = 0, row = 1, padx = 20, pady = 20)
add_task_button = Button(task_label, text = "Import the tasks").grid(column = 0, row = 0)
man_task_button = Button(task_label, text = "Add a task manually").grid(column = 0, row = 1)
del_task_button = Button(task_label, text = "Delete a task").grid(column = 0, row = 2)

for button in task_label.winfo_children():
    button.grid_configure(padx = 20, pady = 10, sticky = "ew")

data_int_label = LabelFrame(left_frame, text = "Data logs")
data_int_label.grid(column = 0, row = 2, padx = 20, pady = 20)
logs_label = Label(data_int_label, text = "Should be display all logs").grid(column = 0, row = 0, padx=10, pady=10)

planning = LabelFrame(right_frame, text="Planning")
planning.grid(column = 0, row = 0, padx = 20, pady = 20)

month_label = Label(planning, text = "Month/Day").grid(column = 0, row = 0)
hour = Label(planning, text = "Hour").grid(column = 1, row = 0)
task_name = Label(planning, text = "Task name").grid(column = 2, row = 0)
name = Label(planning, text = "Employee").grid(column = 3, row = 0)
target_date = Label(planning, text = "Target date").grid(column = 4, row = 0)


for widget in planning.winfo_children():
    widget.grid(padx=50)
    
root.mainloop()