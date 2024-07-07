#NOTE: Check colours at https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
#NOTE: Do NOT use JPEG files (it doesn't work straight out of the box - stick to PNG files!)

from tkinter import * 

root = Tk()
root.title("Moose") #Doggo
root.config(bg="deepskyblue4")

#Create left and right frames
left_frame = Frame(root, width=200, height=400, bg="skyblue3")
left_frame.grid(row=0, column=0, padx=10, pady=5) #padx and pady add padding to ensure not everything is cluttered together

right_frame = Frame(root, width=650, height=400, bg='skyblue3')
right_frame.grid(row=0, column=1, padx=10, pady=5)

#Create frames and labels in left frame
Label(left_frame, text="Moose the Malamute", bg="skyblue3").grid(row=0, column=0, padx=5, pady=5)

#Load image to be 'edited'
image = PhotoImage(file="images/moose.png")
original = image.subsample(3, 3)
Label(left_frame, image=original).grid(row=0, column=0, padx=5, pady=5)

#Display image in right frame
full_img = image.subsample(2, 2) #The image was enormous, had to half its size
Label(right_frame, image=full_img).grid(row=0, column=0, padx=5, pady=5)

#Create tool bar frame
tool_bar = Frame(left_frame, width=180, height = 185, bg="lightskyblue1") 
tool_bar.grid(row=2, column=0, padx=5, pady=5)

#Placeholder labels for other widgets
Label(tool_bar, text='Tools', relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10) #ipadx is INSIDE padding
Label(tool_bar, text='Filters', relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

#Example labels which could be under 'Tool' menu
Label(tool_bar, text='Select').grid(row=1, column=0, padx=5, pady=5)
Label(tool_bar, text='Crop').grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text='Rotate & Flip').grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text='Resize').grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text='Exposure').grid(row=5, column=0, padx=5, pady=5)

root.mainloop()