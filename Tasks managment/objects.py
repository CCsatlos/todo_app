from interface import MainFrames, Add_Del_Button, root

class Employee:
    def __init__(self):
        self.employee_list = {}

    def add_employee(self):
        self.f_name = Add_Del_Button.f_name
        self.l_name = Add_Del_Button.l_name
        
        print (self.f_name, self.l_name)


class Task:
    def __init__(self):
        pass

frame1 = MainFrames(root)
command = Add_Del_Button.save(command = Employee.add_employee)
root.mainloop()