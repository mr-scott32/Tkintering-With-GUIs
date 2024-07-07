# Importing the necessary modules from tkinter library
from tkinter import *
from tkinter import messagebox

# Creating the main window for the application
root = Tk()
# Setting the title of the window
root.title("Practice Grid")
# Setting the size of the window
root.geometry("210x180")

# Defining a function to display the selected checkbox values
def displayChecked():
    # Retrieving the current values of the checkboxes
    red = red_var.get()
    yellow = yellow_var.get()
    green = green_var.get()
    blue = blue_var.get()

    # Displaying a message box with the selected values
    messagebox.showinfo('Colour Choices', f"Red: {red}\nYellow:{yellow}\nGreen: {green}\nBlue: {blue}")

# Creating a label widget with the specified text and placing it in the grid
label = Label(root, text="Which colours do you like below?")
label.grid(row=0)

# Creating variables to store the state of each checkbox
red_var = IntVar()
yellow_var = IntVar()
green_var = IntVar()
blue_var = IntVar()

# Creating checkbuttons for each colour, linking them to the respective variables, setting their background colours, and placing them in the grid
Checkbutton(root, width=10, text='red', variable=red_var, bg='red').grid(row=1)
Checkbutton(root, width=10, text='yellow', variable=yellow_var, bg='yellow').grid(row=2)
Checkbutton(root, width=10, text='green', variable=green_var, bg='green').grid(row=3)
Checkbutton(root, width=10, text='blue', variable=blue_var, bg='blue').grid(row=4)

# Creating buttons for 'Tally' and 'End', linking them to their respective commands, and placing them in the grid
Button(root, text='Tally', command=displayChecked).grid(row=5)
Button(root, text='End', command=root.quit).grid(row=6)

# Running the Tkinter event loop
root.mainloop()
