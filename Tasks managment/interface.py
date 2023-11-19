from tkinter import ttk
from tkinter import Tk, Frame, Label, Button

root = Tk()
root.geometry("1100x800")
root.title("Task Management")
root.config(bg="white")
root.resizable(1, 1)


frame1 = Frame(root, background="#7FFFD4")
frame1.grid(ipadx=100, ipady=390, padx=10, pady=10, sticky="nw")
frame2 = Frame(root, background="#16E2F5")
frame2.grid(ipadx=270, ipady=390,  padx=10, pady=10, row=0, column=1)
frame2.pack_propagate(False)



the_button = Button(frame1, text="Button", background = "#16E2F5")
the_button.grid(ipadx=50, ipady=5, padx=10, pady=10, sticky="n")

row_date = 0
row_hour = 0
row_name = 0



for date_frame in range(0, 10):
    date_frame = Frame(frame2, background="white")
    date_frame.grid(ipadx=70, ipady=10, padx=5, pady=5, row=row_date, column=0)
    row_date += 1

for name_frame in range(0, 10):
    date_frame = Frame(frame2, background="white")
    date_frame.grid(ipadx=40, ipady=10, padx=5, pady=5, row=row_hour, column=1)
    row_hour += 1

for name_frame in range(0, 10):
    date_frame = Frame(frame2, background="white")
    date_frame.grid(ipadx=100, ipady=10, padx=5, pady=5, row=row_name, column=2)
    row_name += 1
    


root.mainloop()