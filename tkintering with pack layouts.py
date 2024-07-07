from tkinter import *

root = Tk()
root.title('Using Pack')
root.geometry("300x100")
root.config(bg='skyblue')

button1 = Button(root, text='Click Me!')
button1.pack(side='left')

label1 = Label(root, text='Read Me!', bg='skyblue')
label1.pack(side='right')
label2 = Label(root, text='Hello!', bg='skyblue2')
label2.pack(side='right')

def toggled():
    print('The check button. It works.')

var = IntVar() #This will check if the checkbox is clicked or not
check = Checkbutton(root, text='Click Me!', bg='skyblue', command=toggled, variable=var, anchor='w')
check.pack(side='bottom')

root.mainloop()


