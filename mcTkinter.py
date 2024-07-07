import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
from tkinter import messagebox

#Setup Tkinter
root = Tk()
root.title('Big Mac Data Dump')
root.minsize(200, 150)
root.maxsize(400, 350)
root.geometry('400x350+850+200')
root.config(bg='tomato')

#Setup data with Matplotlib
big_mac_df = pd.read_csv('data/big_mac_aud.csv',
                            header=None,
                            names=['Country', 'Local', 'AUD', 'Date'])

#Define functions
def showMean():
    aud_mean = big_mac_df['AUD'].mean()
    messagebox.showinfo('Mean', f'The mean price of a Big Mac in AUD is {aud_mean}')
                           
def showMedian():
    aud_median = big_mac_df['AUD'].median()
    messagebox.showinfo('Mean', f'The mean price of a Big Mac in AUD is {aud_median}')               

def showBigMac():
    big_mac_df.plot(
                    kind='bar',
                    x='Country',
                    y='AUD',
                    color='blue',
                    alpha=0.3,
                    title='Cost of a Big Mac in AUD')
    plt.tight_layout()
    plt.show()

image = PhotoImage(file='images/big mac.png')  # Load an image from a file
img_resize = image.subsample(10, 10)  # Resize the image
Label(root, image=img_resize, bg='white', relief=SUNKEN).pack(side=TOP, padx=5, pady=5)

#Create buttons and call functions
show_bm = Button(root, text='Big Mac Cost (AUD)', bg='yellow', command=showBigMac)  
show_mean = Button(root, text='Show Mean AUD Price', bg='yellow', command=showMean)
show_median = Button(root, text='Show Median AUD Price', bg='yellow', command=showMedian)
quit = Button(root, text='Exit', bg='yellow', command=root.quit)

# Add all buttons and labels to a list for packing
btn_pack = [show_bm, show_mean, show_median, quit]


# Pack all buttons and labels at once
for btn in btn_pack:
    btn.pack(side=TOP, padx=5, pady=5)  # Add the widget to the window and make it visible

root.mainloop()  # Run the main event loop to listen for events (like button clicks)