import tkinter as tk
import webbrowser
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x200")

root.title('SRM Institute of Science and Technology')
root.iconbitmap('C:\\Users\\pawan\\Desktop\\chatbot for student\\images\\srm logo.ico')

root.configure(background='#0096DC')
# img = Image.open('srm_logo.png')
# resized_img = img.resize((70,70))
# img = ImageTk.PhotoImage(resized_img)

logo = tk.PhotoImage(file="images\\Srmseal.png")
logo_label = tk.Label(root, image=logo)
logo_label.pack(side="top", pady=10)



# Define functions to connect to websites
def connect_to_attendance():
    webbrowser.open("https://q.srmcheck.me/attendance")

def connect_to_results():
    webbrowser.open("https://q.srmcheck.me/marks")

def connect_to_events():
    webbrowser.open("https://academia.srmist.edu.in/#Academic_Reports")

# Add buttons for attendance, results, and events

bg_image = tk.PhotoImage(file="images\\campus.png")
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

root.maxsize(500,500)
root.minsize(500,500)

btn_send = Button(root, text='attaindance', command=connect_to_attendance, width=15, height=3)
btn_send.place(relx=0.20, rely=0.95, anchor='s')

btn_clear = Button(root, text='Result', command=connect_to_results, width=15, height=3)
btn_clear.place(relx=0.50, rely=0.95, anchor='s')

btn_clear = Button(root, text='events', command=connect_to_events, width=15, height=3)
btn_clear.place(relx=0.80, rely=0.95, anchor='s')

root.mainloop()
