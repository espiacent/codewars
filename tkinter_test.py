from logging import root
import tkinter
from tkinter import messagebox

#main window
TOP = tkinter.Tk()
TOP.title('First GUI')

# top.geometry('300x300+50+50')
window_width = 300
window_height = 300

# get the screen dimension
screen_width = TOP.winfo_screenwidth()
screen_height = TOP.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
TOP.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#button click
def hello_world():
    messagebox.showinfo( "Hello Python", "Hello World")

#button
hello_button = tkinter.Button(TOP, text ="Hello", command = hello_world)
hello_button.pack(pady=50)

exit_button = tkinter.Button(TOP, text="Bye", command=TOP.destroy)
exit_button.pack(pady=50)

TOP.mainloop()