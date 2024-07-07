from tkinter import *

root = Tk()
root.title("Profile Entry using Grid")
root.geometry("500x300")  # set starting size of window
root.maxsize(500, 300)  # width x height
root.config(bg="lightgrey")

# Profile picture
image = PhotoImage(file="images/profile.png")
small_img = image.subsample(4,4)

img = Label(root, image=small_img)
img.grid(row=0, column=0, rowspan=6, padx=5, pady=5)

# Enter specific information for your profile into the following widgets
enter_info = Label(root, text="Please enter your information: ", bg="lightgrey")
enter_info.grid(row=0, column=1, columnspan=4, padx=5, pady=5)

# Name label and entry widgets
Label(root, text="Name", bg="lightgrey").grid(row=1, column=1, padx=5, pady=5, sticky=E)

name = Entry(root, bd=3)
name.grid(row=1, column=2, padx=5, pady=5)

# Gender label and dropdown widgets

Label(root, text="Gender", bg="lightgrey").grid(row=2, column=1, padx=5, pady=5, sticky=E)

#NOTE: Try this method instead of what is shown on the website, OptionMenu works much more effectively for this task!
gender_var = StringVar(root)
gender_var.set('Select')
gender_menu = OptionMenu(root, gender_var, 'Male', 'Female', 'Non-Binary')
gender_menu.grid(row=2, column=2, padx=5, pady=5, sticky=W)


# Eyecolor label and entry widgets
Label(root, text="Eye Color", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5, sticky=E)
eyes = Entry(root, bd=3)
eyes.grid(row=3, column=2, padx=5, pady=5)

# Height and Weight labels and entry widgets
Label(root, text="Height", bg="lightgrey").grid(row=4, column=1, padx=5, pady=5, sticky=E)
Label(root, text="inches", bg="lightgrey").grid(row=4, column=3, sticky=W)

height = Entry(root, bd=3)
height.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()