from tkinter import *  # Import all functions and classes from tkinter
from tkinter import messagebox  # Import message box for displaying messages

root = Tk()  # Create the main application window
root.title("Login to Wash Dog")  # Set the title of the main window
root.geometry('500x500')  # Set the size of the window
root.maxsize(500, 500)  # Set the maximum size of the window
root.config(bg='#6FAFE7')  # Set the background color of the window

# Create a label for the login title
login = Label(root, text='Login to Wash Dog', bg='#2176C1', fg='white', relief=RAISED)
login.pack(ipady=5, fill='x')  # Add the label to the window and make it visible
login.config(font=('Font', 30))  # Set the font and size of the label text

# Load and display an image
image = PhotoImage(file='images/moose.png')  # Load an image from a file
img_resize = image.subsample(5, 5)  # Resize the image
Label(root, image=img_resize, bg='white', relief=SUNKEN).pack(pady=5)  # Add the image to the window

# Define a function to display a new window with a washed dog image
def washDog():
    window = Toplevel(root)  # Create a new top-level window
    window.title('Dog Washed!')  # Set the title of the new window
    image = PhotoImage(file='images/clean moose.png')  # Load an image from a file
    image = image.subsample(2, 2)  # Resize the image

    original = Label(window, image=image)  # Create a label to display the image
    original.image = image  # Keep a reference to the image to prevent garbage collection
    original.pack()  # Add the label to the window and make it visible

# Define a function to check the username and password
def checkInput():
    user = 'Username301'  # Set the correct username
    pwd = 'Passw0rd'  # Set the correct password
    user_ent = username_entry.get()  # Get the entered username
    pwd_ent = password_entry.get()  # Get the entered password

    if user == user_ent and pwd == pwd_ent:  # Check if the entered username and password are correct
        washDog()  # Call the washDog function to display the washed dog
    else:
        messagebox.showerror('Login failed!', 'You are a failure! SHUT IT DOWN!')  # Show an error message
        root.destroy()  # Close the main window

# Define a function to print a message when the checkbox is toggled
def toggled():
    print('The check button works!')

# Create a frame for the username entry
user_frame = Frame(root, bg='#6FAFE7')
user_frame.pack()  # Add the frame to the window

# Create a label and entry for the username
Label(user_frame, text='Username', bg='#6FAFE7').pack(side='left', padx=5)
username_entry = Entry(user_frame, bd=3)
username_entry.pack(side='left')

# Create a frame for the password entry
pwd_frame = Frame(root, bg='#6FAFE7')
pwd_frame.pack()  # Add the frame to the window

# Create a label and entry for the password
Label(pwd_frame, text='Password', bg='#6FAFE7').pack(side='left', padx=7)
password_entry = Entry(pwd_frame, bd=3, show='*')  # Mask the password entry
password_entry.pack(side='left')

# Create a button to submit the login details
go_btn = Button(root, text='GO!', command=checkInput, bg='#6FAFE7', width=15)
go_btn.pack(pady=5)  # Add the button to the window

# Create a frame for the bottom section
bottom_frame = Frame(root, bg='#6FAFE7')
bottom_frame.pack()  # Add the frame to the window

# Create a checkbox for "Remember me" functionality
var = IntVar()  # Variable to store the checkbox state
remember_me = Checkbutton(bottom_frame, text='Remember me', bg='#6FAFE7', command=toggled, variable=var)
remember_me.pack(side='left', padx=19)  # Add the checkbox to the window

root.mainloop()  # Run the main event loop to listen for events (like button clicks)
