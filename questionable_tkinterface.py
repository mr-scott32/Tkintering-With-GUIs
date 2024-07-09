from tkinter import *
from tkinter import messagebox
#Global variables
escaped = False
door_key = False
game_over = False

#Setup main screen
root = Tk()
root.title('Questionable Tkinterface')
root.maxsize(700, 700)
root.config(bg='peachpuff2')
map = PhotoImage(file='qtgfx/map.png')
map_lbl = Label(root, image=map, bg='white', relief=SUNKEN).grid(row=0, column=0, columnspan=3)

def closeOnlyScreen(img_path, msg, txt, img_size):
    window = Toplevel(root)
    window.title(txt)
    window.config(bg='peachpuff2')
    img = PhotoImage(file=img_path)
    img = img.subsample(img_size, img_size)
    img_label = Label(window, image=img, bg='peachpuff2', relief=SUNKEN)
    img_label.grid(row=0, column=0, columnspan=3)
    img_label.image = img

    T = Text(window, height=3, width=45, bg='bisque')
    T.grid(column=1, row=2)
    t_lbl = Label(window, text=txt, bg='peachpuff2').grid(column=1, row=1, padx=5, pady=5)
    T.insert(END, msg)

    close_btn = Button(window, text='Close', command=window.destroy, bg='peachpuff4').grid(column=1, row=4, padx=5, pady=5)

def decisionScreen(img_path, msg, txt, img_size, btn_img, btn_msg, btn_txt, btn_size):
    window = Toplevel(root)
    window.title(txt)
    window.config(bg='peachpuff2')
    img = PhotoImage(file=img_path)
    img = img.subsample(img_size, img_size)
    img_label = Label(window, image=img, bg='peachpuff2', relief=SUNKEN)
    img_label.grid(row=0, column=0, columnspan=3)
    img_label.image = img

    T = Text(window, height=3, width=45, bg='bisque')
    T.grid(column=1, row=2)
    t_lbl = Label(window, text=txt, bg='peachpuff2').grid(column=1, row=1, padx=5, pady=5)
    T.insert(END, msg)
    
    y_btn = Button(window, text='Yes', command= lambda: gameOver(btn_img, btn_msg, btn_txt, btn_size, window), 
                   bg='peachpuff4').grid(column=0, row=5, padx=5, pady=5, sticky=E)
    
    n_btn = Button(window, text='No', command=window.destroy, bg='peachpuff4').grid(column=2, row=5, padx=5, pady=5, sticky=W)

def gameOver(img_path, msg, txt, size, wind):
    global game_over
    game_over = True
    wind.destroy()
    window = Toplevel(root)
    window.title('AHHHH!')
    window.config(bg='peachpuff2')
    img = PhotoImage(file=img_path)
    img = img.subsample(size, size)
    img_label = Label(window, image=img, bg='peachpuff2', relief=SUNKEN)
    img_label.grid(row=0, column=0, columnspan=3)
    img_label.image = img

    T = Text(window, height=3, width=45, bg='bisque')
    T.grid(column=1, row=2)
    t_lbl = Label(window, text=txt, bg='peachpuff2').grid(column=1, row=1, padx=5, pady=5)
    T.insert(END, msg)
    close_btn = Button(window, text='Close', command=closeProgram, bg='peachpuff4').grid(column=1, row=4, padx=5, pady=5)  
    
def closeProgram():
    global game_over
    if game_over == True:
        messagebox.showwarning('You have died!', 'Death comes for us all!')
        root.destroy()

def poolDecision(img_path, msg, txt, img_size, btn_img, btn_msg, btn_txt, btn_size):
    window = Toplevel(root)
    window.title(txt)
    window.config(bg='peachpuff2')
    img = PhotoImage(file=img_path)
    img = img.subsample(img_size, img_size)
    img_label = Label(window, image=img, bg='peachpuff2', relief=SUNKEN)
    img_label.grid(row=0, column=0, columnspan=3)
    img_label.image = img

    T = Text(window, height=3, width=45, bg='bisque')
    T.grid(column=1, row=2)
    t_lbl = Label(window, text=txt, bg='peachpuff2').grid(column=1, row=1, padx=5, pady=5)
    T.insert(END, msg)
    
    y_btn = Button(window, text='Yes', command= lambda: poolHint(btn_img, btn_msg, btn_txt, btn_size, window), 
                   bg='peachpuff4').grid(column=0, row=5, padx=5, pady=5, sticky=E)
    
    n_btn = Button(window, text='No', command=window.destroy, bg='peachpuff4').grid(column=2, row=5, padx=5, pady=5, sticky=W)

def poolHint(img_path, msg, txt, size, wind):
    wind.destroy()
    window = Toplevel(root)
    window.title('Water Dragon')
    window.config(bg='peachpuff2')
    img = PhotoImage(file=img_path)
    img = img.subsample(size, size)
    img_label = Label(window, image=img, bg='peachpuff2', relief=SUNKEN)
    img_label.grid(row=0, column=0, columnspan=3)
    img_label.image = img

    T = Text(window, height=3, width=45, bg='bisque')
    T.grid(column=1, row=2)
    t_lbl = Label(window, text=txt, bg='peachpuff2').grid(column=1, row=1, padx=5, pady=5)
    T.insert(END, msg)
    close_btn = Button(window, text='Close', command=window.destroy, bg='peachpuff4').grid(column=1, row=4, padx=5, pady=5)

def southDoor(img_path, msg, txt, size):
    window = Toplevel(root)
    window.title('South Door')
    window.config(bg='peachpuff2')
    img = PhotoImage(file=img_path)
    img = img.subsample(size, size)
    img_label = Label(window, image=img, bg='peachpuff2', relief=SUNKEN)
    img_label.grid(row=0, column=0, columnspan=3)
    img_label.image = img

    T = Text(window, height=3, width=45, bg='bisque')
    T.grid(column=1, row=2)
    t_lbl = Label(window, text=txt, bg='peachpuff2').grid(column=1, row=1, padx=5, pady=5)
    T.insert(END, msg)

    user_ans = Entry(window)
    user_ans.grid(column=1, row=5, padx=5, pady=5)
    enter_btn = Button(window, text='Enter', command=lambda: checkInput(user_ans, window), bg='peachpuff4').grid(column=1, row=6, padx=5, pady=5)



def checkInput(user_ans, wind):
    global door_key

    user_input = user_ans.get()
    ans = 'die'
    try:
        if user_input == ans:
            door_key = True
            messagebox.showinfo('Key Obtained!', 'You obtained a door key!')
        else:
            messagebox.showinfo('AHHH!', 'You have been vaporised, there is nothing left!')
            root.destroy()

    except:  
        messagebox.showinfo('AHHH!', 'Too lazy to even bother replying? BEGONE! DIE!')
        root.destroy()  
    
    wind.destroy()

def exitDoor(img_path, img_size):
    global door_key, escaped
    window = Toplevel(root)
    window.title('Locked Door')
    window.config(bg='peachpuff2')
    img = PhotoImage(file=img_path)
    img = img.subsample(img_size, img_size)
    img_label = Label(window, image=img, bg='peachpuff2', relief=SUNKEN)
    img_label.grid(row=0, column=0, columnspan=3)
    img_label.image = img

    T = Text(window, height=3, width=45, bg='bisque')
    T.grid(column=1, row=2)

    if door_key == True:
        
        t_lbl = Label(window, text='Freedom!', bg='peachpuff2').grid(column=1, row=1, padx=5, pady=5)
        msg = 'You used your key to open the door!'
        T.insert(END, msg)
        escaped = True
        close_btn = Button(window, text='Close', command=escapeDungeon, bg='peachpuff4').grid(column=1, row=4, padx=5, pady=5)   
        
    else:
        t_lbl = Label(window, text='Locked Door', bg='peachpuff2').grid(column=1, row=1, padx=5, pady=5)
        msg = 'Oops! This door is locked!'
        T.insert(END, msg)
        close_btn = Button(window, text='Close', command=window.destroy, bg='peachpuff4').grid(column=1, row=4, padx=5, pady=5)   

def escapeDungeon():
    global escaped
    if escaped == True:
        messagebox.showinfo('You won!', 'You have escaped the dungeon!')
        root.destroy()

def setupButtons():
#We use 'lambda' if we want to pass parameters to our functions in a Button command.
    statue_btn = Button(root, text='Check Statue', 
                        command=lambda: closeOnlyScreen(
                        'qtgfx/statue.png','If you open the chest, you will discover its \neffects.','Statue of Solace', 1), 
                        bg='peachpuff4', width=15).grid(row=2, column=2, padx=5, pady=5, sticky=S) 

    curtain_btn = Button(root, text='Check Curtain',
                        command=lambda: closeOnlyScreen(
                        'qtgfx/curtain.png','Open the sarcophagus to discover infinite \nemeralds.','Curious Curtain', 1),
                        bg='peachpuff4', width=15).grid(row=2, column=0, padx=5, pady=5, sticky=S)

    west_btn = Button(root, text='West Door',
                        command=lambda: closeOnlyScreen(
                        'qtgfx/shadow door.png',
                        'It seems this part of the game has not been \nbuilt yet. Oh well. Find the secret of the \nnorth door to deliver its exit.',
                        'The Shadow', 2), bg='peachpuff4', width=15).grid(row=3, column=0, padx=5, pady=5, sticky=S)

    chest_btn = Button(root, text='Check Chest', command=lambda: decisionScreen(
                        'qtgfx/chest.png', 'Do you wish to open the chest?', 'Chest', 1,
                        'qtgfx/mimic.png', 'It was a mimic! You have been consumed!', 'NOM NOM NOM', 5),
                        bg='peachpuff4', width=15).grid(row=4, column=2, padx=5, pady=5, sticky=S)

    north_btn = Button(root, text='North Door', command=lambda: decisionScreen(
                        'qtgfx/deaddoor.png', 'Do you wish to continue forward?', 'Ominous Door', 3,
                        'qtgfx/doormimic.png', 'It was a mimic! You have been consumed!', 'NOM NOM NOM', 1),
                        bg='peachpuff4', width=15).grid(row=2, column=1, padx=5, pady=5, sticky=S)

    sarc_btn = Button(root, text='Sarcophagus', command=lambda: decisionScreen(
                        'qtgfx/sarcophagus.png', 'Do you wish to check for treasure?', 'Sarcophagus', 2,
                        'qtgfx/undead.png', 'The undead knight rises and strikes you down!\nShould have let him rest...', 'Who disturbs my slumber?', 3),
                        bg='peachpuff4', width=15).grid(row=3, column=1, padx=5, pady=5, sticky=S)

    pool_btn = Button(root, text='Pool', command=lambda: poolDecision(
                        'qtgfx/pool.png', 'This pool seems to lead somewhere. \Would you like to swim through?', 'Cave Pool', 2,
                        'qtgfx/dragon.png', '"The last three words of each devious hint \nwill grant you the knowledge you seek."', 'You found a water dragon!?', 3),
                        bg='peachpuff4', width=15).grid(row=4, column=0, padx=5, pady=5, sticky=S)

    south_btn = Button(root, text='South Door', command=lambda: southDoor(
                        'qtgfx/shield door.png', 'The door glows. "What is the password?"', 'Glowing Door', 2),
                        bg='peachpuff4', width=15).grid(row=4, column=1, padx=5, pady=5, sticky=S)


    east_btn = Button(root, text='East Door', 
                    command=lambda: exitDoor(
                    'qtgfx/exit.png', 3), 
                    bg='peachpuff4', width=15).grid(row=3, column=2, padx=5, pady=5, sticky=S) 




if __name__ == "__main__":
    setupButtons()
    root.mainloop()