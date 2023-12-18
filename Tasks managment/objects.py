from interface import MainFrames, Add_Del_Button, root


class Employee_Manager:
    def __init__(self):
        self.employee_list = {}
    
    def add_employee(self):
        self.first_name = add_button.f_name.get()
        self.working_hours = add_button.w_hours.get()
        #self.employee_list[self.first_name] = self.working_hours
        print(f"{self.first_name} and {self.working_hours}")
        
        #print(self.employee_list)


frame = MainFrames(root)
the_employee_manager = Employee_Manager()
add_button = Add_Del_Button(frame)
add_button.save.config(command = the_employee_manager.add_employee())
add_button.save.destroy()
root.mainloop()


        
    

