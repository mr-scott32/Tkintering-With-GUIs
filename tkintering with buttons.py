from tkinter import *  # Import all functions and classes from tkinter
from tkinter.ttk import *  # Import all functions and classes from tkinter.ttk

root = Tk()  # Create the main application window

# Define a function to increase the volume
def volumeUp():
    print('Volume Increase +1')  

# Define a function to decrease the volume
def volumeDown():
    print('Volume Decrease -1') 

# Define a function to turn on the TV
def turnOn():
    window = Toplevel(root)  # Create a new top-level window
    window.title('TV')  # Set the title of the new window
    image = PhotoImage(file='images/moose.png')  # Load an image from a file

    original = Label(window, image=image)  # Create a label to display the image
    original.image = image  # Keep a reference to the image to prevent garbage collection
    original.pack()  # Add the label to the window and make it visible

# Define a function to create a button with an image
def imgBtn(imgpath, sub_no, cmd):
    img = PhotoImage(file=imgpath)  # Load an image from a file
    photo = img.subsample(sub_no, sub_no)  # Subsample the image to make it smaller
    btn = Button(root, image=photo, command=cmd)  # Create a button with the image and a command
    photo.image = photo  # Keep a reference to the image to prevent garbage collection
    return btn  # Return the button

# Create a TV remote
turn_on = imgBtn('images/on.png', 8, turnOn)  # Create a button to turn on the TV
turn_off = imgBtn('images/off.png', 10, root.quit)  # Create a button to quit the application

volume = Label(text="VOLUME")  # Create a label for volume control
vol_up = Button(root, text="+", command=volumeUp)  # Create a button to increase the volume
vol_down = Button(root, text="-", command=volumeDown)  # Create a button to decrease the volume

# Add all buttons and labels to a list for packing
to_pack = [turn_on, turn_off, volume, vol_up, vol_down]

# Pack all buttons and labels at once
for item in to_pack:
    item.pack()  # Add the widget to the window and make it visible

root.mainloop()  # Run the main event loop to listen for events (like button clicks)
