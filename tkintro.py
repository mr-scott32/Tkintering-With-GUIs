from tkinter import * #Import tkinter module

root = Tk() #Create a root widget - the parent window, has to be created before others
root.title("Tkintro")
root.configure(background="skyblue") #set background colour
root.minsize(200, 200) #width, height
root.maxsize(500, 500)
root.geometry("800x800+750+150") #width x height + x + y - width and height set size of window, x and y sets coordinates of where it will appear on the screen (0,0 is top left)


#Now let's give it a label - there are other ways to position it, but for now we'll just have the text fit top and centre. 
text = Label(root, text='"Is mayonnaise an instrument?"')
text.pack() #Pack fits the size of the window to the text, 'packing' the text into the parent window
text2 = Label(root, text="- Patrick Star")
text2.pack()

patrick = PhotoImage(file="images/patrick.png") #Loads the image into a variable called 'patrick'
patrick_label = Label(root, image=patrick) #Stores label into 'patrick_label' variable and attaches it to 'patrick' image. 
patrick_label.pack() #Packs the image by accessing its label, similar to the text.


root.mainloop() #This one generates and shows the root window

