from tkinter import ttk
from tkinter import Tk, Frame, Label, Button, LabelFrame, Toplevel, Entry


root = Tk()
root.title("Task Manager")
root.config(bg = "white")
# root.resizable(0, 0)

class MainFrames:

    def __init__(self, master):
        self.left_frame = Frame(master, name = "left frame")
        self.left_frame.grid(column = 0, row = 0)
        self.right_frame = Frame(master, name = "right frame")
        self.right_frame.grid(column = 1, row = 0, sticky = "n")
        self.labels()

    def labels(self):
        label_1 = EmployeesLabel(self.left_frame)
        label_2 = TaskLabel(self.left_frame)
        label_3 = LogsFrame(self.left_frame)
        label_4 = PlaningLabel(self.right_frame)

class EmployeesLabel:

    def __init__(self, master):
        self.emp_label = LabelFrame(master, text = "Employees")
        self.emp_label.grid(column = 0, row = 0, padx = 20, pady = 20)
        self.all_emp_button = Button(self.emp_label, text = "Select all employees")
        self.select_button = Button(self.emp_label, text = "Select the employees")
        self.add_del_button = Button(self.emp_label, text = "Add/delete an employee", command = self.open_window)
        self.placing_buttons()
    
    def placing_buttons(self):
        place = 0
        for button in self.emp_label.winfo_children():
            button.grid(column = 0, row = place, padx = 20, pady = 10, sticky = "ew")
            place += place + 1

    def open_window(self):
        new_window = Add_Del_Button(self.add_del_button)

class Add_Del_Button:

    def __init__(self, master):
        self.top_lvl = Toplevel(master)
        self.top_lvl.geometry("450x200+160+120")
        self.label_f_name = Label(self.top_lvl, text = "First name")
        self.label_l_name = Label(self.top_lvl, text = "Last name")
        self.label_w_hours = Label(self.top_lvl, text = "Working hours")
        self.f_name = Entry(self.top_lvl)
        self.l_name = Entry(self.top_lvl)
        self.w_hours = Entry(self.top_lvl)
        self.save = Button(self.top_lvl, text = "Print and quit")
        self.placing_labels()
        self.placing_entries()

    def placing_labels(self):
        label_widgets = [self.label_f_name, self.label_l_name, self.label_w_hours]
        for place, widget in enumerate(label_widgets):
            widget.grid(column = 0, row = place, padx = 10, pady = 5)
    
    def placing_entries(self):
        entries = [self.f_name, self.l_name, self.w_hours, self.save]
        for place, widget in enumerate(entries):
            widget.grid(column = 1, row = place, padx = 10, pady = 5)

class TaskLabel:

    def __init__(self, master):
        self.task_label = LabelFrame(master, name = "task label")
        self.task_label.grid(column = 0, row = 1, padx = 20, pady = 20)
        self.import_task = Button(self.task_label, text = "Import the tasks")
        self.add_task = Button(self.task_label, text = "add a tasks")
        self.del_task = Button(self.task_label, text = "Delete a tasks")

        self.placing_buttons()
    
    def placing_buttons(self):
        buttons = [self.import_task, self.add_task, self.del_task]
        for place, button in enumerate(buttons):
            button.grid(column = 0, row = place, padx = 20, pady = 10, sticky = "ew")

class LogsFrame:

    def __init__(self, master):
        self.logs_frame = LabelFrame(master, text = "Data logs")
        self.logs_frame.grid(column = 0, row = 2, padx = 20, pady = 20)
        self.logs_label = Label(self.logs_frame, text = "Should be display the last few logs")
        self.logs_label.grid(column = 0, row = 0, padx=10, pady=10)

class PlaningLabel:
    def __init__(self, master):
        self.planing = LabelFrame(master, text = "Planing")
        self.planing.grid(column = 1, row = 0, padx=20, pady=20)
        self.month_label = Label(self.planing, text = "Month/Day")
        self.hour = Label(self.planing, text = "Hour")
        self.task_name = Label(self.planing, text = "Task name")
        self.name = Label(self.planing, text = "Employee")
        self.target_date = Label(self.planing, text = "Target date")
        self.placing_labels()
    
    def placing_labels(self):
        labels = [self.month_label, self.hour, self.task_name, self.name, self.target_date]
        for place, label in enumerate(labels):
            label.grid(column=place, row=0, padx=50, pady=20)

frame1 = MainFrames(root)
root.mainloop()
      