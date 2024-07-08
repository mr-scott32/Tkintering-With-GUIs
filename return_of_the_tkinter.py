import tkinter as tk     
from game_objects import Player, Enemy, Weapon
from tkinter import *          
from tkinter import font as tkfont 
from tkinter import messagebox
import random


class tkinterTrial(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage, FightScreen, Movement):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def refresh_frame(self, page_name):
        '''Refresh a frame for the given page name'''
        frame = self.frames[page_name]
        frame.destroy()
        frame_class = eval(page_name)
        new_frame = frame_class(parent=self.container, controller=self)
        self.frames[page_name] = new_frame
        new_frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(page_name)
    
    def quit_game(self):
        self.destroy()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select Character", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Gandalf",
                            command=lambda:[self.selectGandalf(), controller.show_frame("Movement")])
        button2 = tk.Button(self, text="Gimli",
                            command=lambda:[self.selectGimli(), controller.show_frame("Movement")])
        button3 = tk.Button(self, text="Legolas",
                            command=lambda:[self.selectLegolas(), controller.show_frame("Movement")])
        button4 = tk.Button(self, text="Aragorn",
                            command=lambda:[self.selectAragorn(), controller.show_frame("Movement")])
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

    def selectGandalf(self):
        global player, weapon
        player = players[0]
        weapon = weapons[0]
        messagebox.showinfo('Character Select', f'You have selected {player.name} the {player.race} {player.cls}! \n You are equipped with {weapon.name}, the {weapon.wpn}')
        
    def selectGimli(self):
        global player, weapon
        player = players[1]
        weapon = weapons[1]
        messagebox.showinfo('Character Select', f'You have selected {player.name} the {player.race} {player.cls}! \n You are equipped with {weapon.name}, the {weapon.wpn}')
        
    def selectLegolas(self):
        global player, weapon
        player = players[2]
        weapon = weapons[2]
        messagebox.showinfo('Character Select', f'You have selected {player.name} the {player.race} {player.cls}! \n You are equipped with {weapon.name}, the {weapon.wpn}')
        
    def selectAragorn(self):
        global player, weapon
        player = players[3]
        weapon = weapons[3]
        messagebox.showinfo('Character Select', f'You have selected {player.name} the {player.race} {player.cls}! \n You are equipped with {weapon.name}, the {weapon.wpn}')

   


class FightScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=f'Fight {enemy.name}!', font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        T = Text(self, height=5, width=20)
        T.pack()
        stats = f'{enemy.name} has {enemy.health} health points left! You have {player.health} health points left!'
        T.insert(tk.END, stats)
        button = tk.Button(self, text="ATTACK!",
                           command=lambda: [self.Fight(), controller.refresh_frame('FightScreen')])
        button.pack()


    def Fight(self):
        global enemy, player, game_over, enemies_defeated, weapon
        player.health -= enemy.dmg
        enemy.health -= (player.atk + weapon.dmg)
        messagebox.showinfo('Ouch!', f'{enemy.name} deals {enemy.dmg} damage to you! Your health is now {player.health}!')
        messagebox.showinfo('HAAAAAAA!', f'You have dealt {player.atk + weapon.dmg} with {weapon.name}! The enemy is now on {enemy.health} health!')


        if enemy.health <= 0:
            messagebox.showinfo('Victory!', f'Congratulations, you beat {enemy.name}!')
            app.quit_game()
        if player.health <= 0:
            messagebox.showinfo('Death!', 'You have fallen!')
            app.quit_game()




class Movement(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.game_board_text = Text(self, height=5, width=20)
        self.game_board_text.pack()
        self.label = tk.Label(self, text="Game Board", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        
        # Initialize game board and display
        self.update_board_display()

        buttonN = tk.Button(self, text="North",
                           command=lambda:[self.moveNorth()])
        buttonN.pack()

        buttonS = tk.Button(self, text="South",
                           command=lambda:[self.moveSouth()])
        buttonS.pack()

        buttonE = tk.Button(self, text="East",
                           command=lambda: [self.moveEast()])
        buttonE.pack()

        buttonW = tk.Button(self, text="West",
                           command=lambda: [self.moveWest()])
        buttonW.pack()


    def update_board_display(self):
        global gameBoard
        gameBoard_str = "\n".join([str(row) for row in gameBoard])
        self.game_board_text.config(state=tk.NORMAL)
        self.game_board_text.delete(1.0, tk.END)
        self.game_board_text.insert(tk.END, gameBoard_str)
        self.game_board_text.config(state=tk.DISABLED)

    def moveNorth(self):
        global playerX,playerY
        if playerX > 0:
            gameBoard[playerX][playerY] = 7
            playerX-=1
            gameBoard[playerX][playerY] = 1
            self.update_board_display()
            self.checkEnemy()
        else:
            messagebox.showwarning('Ouch!', 'You cannot move in that direction!')


    def moveSouth(self):
        global playerX,playerY
        if playerX < 4:
            gameBoard[playerX][playerY] = 7
            playerX += 1
            gameBoard[playerX][playerY] = 1
            self.update_board_display()
            self.checkEnemy()
        else:
            messagebox.showwarning('Ouch!', 'You cannot move in that direction!')


    def moveEast(self):
        global playerX,playerY
        if playerY < 4:
            gameBoard[playerX][playerY] = 7
            playerY += 1
            gameBoard[playerX][playerY] = 1
            self.update_board_display()
            self.checkEnemy()
        else:
            messagebox.showwarning('Ouch!', 'You cannot move in that direction!')

 
    def moveWest(self):
        global playerX,playerY
        if playerY > 0:
            gameBoard[playerX][playerY] = 7
            playerY -= 1
            gameBoard[playerX][playerY] = 1
            self.update_board_display()
            self.checkEnemy()
        else:
            messagebox.showwarning('Ouch!', 'You cannot move in that direction!')

    
    def checkEnemy(self):
        if enemyX == playerX and enemyY == playerY:
            self.controller.show_frame('FightScreen')
            messagebox.showinfo('Prepare Yourself!', f'You encounter {enemy.name} the {enemy.type}!')

players = [Player('Gandalf', 'Human', 'Wizard', 2, 100),
           Player('Gimli', 'Dwarf', 'Fighter', 3, 180),
           Player('Legolas', 'Elf', 'Archer', 1, 120 ),
           Player('Aragorn', 'Human', 'Ranger', 4, 130)]

# Create weapons
weapons =  [Weapon('Glamdring', 'Sword', random.randint(8, 12)), 
            Weapon("Balin's Axe", 'Greataxe', random.randint(12, 15)), 
            Weapon('Bow of the Galadhrim', 'Longbow', random.randint(10, 12)),
            Weapon('Anduril', 'Great Sword', random.randint(10, 14))]

# Create enemies
enemies = [Enemy('Azog', 'Orc Warrior', random.randint(15, 18), random.randint(80, 140)),
           Enemy('Saruman', 'Human Wizard', random.randint(20, 30), random.randint(60, 100))]

game_over = False
player_health = 100
player_attack = 1
player = ''
weapon = ''

enemies_defeated = False

gameBoard = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]

# place the player in the middle of the game board
playerX = 2
playerY = 2
gameBoard[playerX][playerY] = 1



enemy = enemies[random.randint(0, 1)]
player = players[0]

enemyX = random.randint(0, 4)
enemyY = random.randint(0, 4)

while enemyX == playerX and enemyX == playerY:
    enemyX = random.randint(0, 4)
    enemyY = random.randint(0, 4)

gameBoard[enemyX][enemyY] = 2

if __name__ == "__main__":
    app = tkinterTrial()
    app.mainloop()