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

def closeOnlyScreen(img_path, msg, txt):
    window = Toplevel(root)
    window.title(txt)
    window.config(bg='peachpuff2')
    img = PhotoImage(file=img_path)
    img_label = Label(window, image=img, bg='peachpuff2', relief=SUNKEN)
    img_label.grid(row=0, column=0, columnspan=3)
    img_label.image = img

    T = Text(window, height=3, width=45, bg='bisque')
    T.grid(column=1, row=2)
    t_lbl = Label(window, text=txt, bg='bisque').grid(column=1, row=1, padx=5, pady=5)
    T.insert(END, msg)

    close_btn = Button(window, text='Close', command=window.destroy).grid(column=1, row=4, padx=5, pady=5)

def gameOver():
    root.destroy()

def decisionScreen(img_path, msg, txt):
    window = Toplevel(root)
    window.title(txt)
    window.config(bg='peachpuff2')
    img = PhotoImage(file=img_path)
    img_label = Label(window, image=img, bg='peachpuff2', relief=SUNKEN)
    img_label.grid(row=0, column=0, columnspan=3)
    img_label.image = img

    T = Text(window, height=3, width=45, bg='bisque')
    T.grid(column=1, row=2)
    t_lbl = Label(window, text=txt, bg='bisque').grid(column=1, row=1, padx=5, pady=5)
    T.insert(END, msg)

    
#We use 'lambda' if we want to pass parameters to our functions in a Button command.
statue_btn = Button(root, text='Check Statue', 
                    command=lambda: closeOnlyScreen('qtgfx/statue.png',
                    'If you open the chest, you will discover its \neffects.',
                    'Statue of Solace'), 
                    bg='peachpuff4', 
                    width=15).grid(row=2, column=0, padx=5, pady=5, sticky=W) 

curtain_btn = Button(root, text='Check Curtain',
                     command=lambda: closeOnlyScreen('qtgfx/curtain.png',
                    'Open the sarcophagus to discover infinite \nemeralds.',
                    'Curious Curtain'),
                    bg='peachpuff4',
                    width=15).grid(row=2, column=1, padx=5, pady=5, sticky=W)

chest_btn = Button(root, text='Check Chest', bg='peachpuff4', width=15).grid(row=3, column=1, padx=5, pady=5, sticky=W)



if __name__ == "__main__":
    root.mainloop()