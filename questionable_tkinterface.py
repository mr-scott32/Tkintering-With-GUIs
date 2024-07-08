from tkinter import *
from tkinter import messagebox

#Setup main screen
root = Tk()
root.title('Questionable Tkinterface')
root.geometry('550x700+600+150')
root.maxsize(700, 700)
root.config(bg='peachpuff2')

map = PhotoImage(file='qtgfx/map.png')
map_lbl = Label(root, image=map, bg='white', relief=SUNKEN).grid(row=0, column=0, columnspan=3)

def statueScreen():
    window = Toplevel(root)
    window.title('Statue')
    img = PhotoImage(file='qtgfx/statue.png')
    img_label = Label(window, image=img, bg='white', relief=SUNKEN)
    img_label.grid(row=0, column=0, columnspan=3)
    img_label.image = img

    T = Text(window, height=3, width=50)
    T.grid(column=1, row=2)
    t_lbl = Label(window, text='Statue of Solace').grid(column=1, row=1)

    msg = 'If you open the chest, you will discover its \neffects.'
    T.insert(END, msg)



statue_btn = Button(root, text='Check Statue', command=statueScreen, bg='peachpuff4', width=15).grid(row=2, column=0, padx=5, pady=5, sticky=W) 
chest_btn = Button(root, text='Check Chest', bg='peachpuff4', width=15).grid(row=2, column=1, padx=5, pady=5, sticky=W)



if __name__ == "__main__":
    root.mainloop()