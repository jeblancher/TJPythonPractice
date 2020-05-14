# First, we import the necessary modules
from datetime import datetime
from tkinter import *

root = Tk()  # open the window
root.title("Tide Location")  # give it a title

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = {'Norfolk/Hampton Roads', 'Pascagoula', 'Houston', 'Long Island Sound'}
tkvar.set('Norfolk/Hampton Roads')  # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a Location").grid(row=1, column=1)
popupMenu.grid(row=2, column=1)


# on change dropdown value
def change_dropdown(*args):
    tkvar.get()


# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()

x = datetime.today()
calldate = x.strftime("%Y%m%d")
location = tkvar.get()
print(location)
print(calldate)