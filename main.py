from ast import Add
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import tkinter as tk
import sqlite3
import webbrowser


def Enter_pressed(event=None):
    input_get = user_input.get().lower()  # convert user input to lowercase
    print(input_get)
    bot_reply = get_data(input_get)
    if len(input_get.strip()) > 0:
        chat_history.insert(INSERT, '\nYou say:\t%s' % input_get)
    if len(bot_reply.strip()) > 0:
        bot_response.delete(0, END)
        bot_response.insert(0, bot_reply)
        chat_history.insert(INSERT, '\nBot says:\t%s' % bot_reply)
    user_input.delete(0, END)
    chat_history.see(END)
    chat_history.insert(INSERT, '\n')
    return "break"


# Initialize database connection
conn = sqlite3.connect('data.db')
c = conn.cursor()


# Create table to store chatbot data
c.execute('''CREATE TABLE IF NOT EXISTS chatbot_data
             (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')

# Function to add new chatbot data


def add_data(question, answer):
    c.execute(
        "INSERT INTO chatbot_data (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()


# Function to retrieve chatbot data
def get_data(question):
    c.execute("SELECT answer FROM chatbot_data WHERE question=?", (question,))
    result = c.fetchone()
    return result[0] if result else "I'm sorry, I don't know the answer to that. Can you ask me something else?"


# Function to update chatbot data
def update_data(id, question, answer):
    c.execute("UPDATE chatbot_data SET question=?, answer=? WHERE id=?",
              (question, answer, id))
    conn.commit()

# Function to authenticate admin


def admin_login(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False


# Function to handle admin commands
def handle_admin_command():
    username = admin_username.get()
    password = admin_password.get()
    if admin_login(username, password):
        admin_window = tk.Toplevel(root)
        admin_window.title("Admin Dashboard")
        admin_window.configure(background='#0096DC')
        admin_window.maxsize(400, 400)
        admin_window.minsize(400, 400)

        # Add data form
        add_frame = tk.Frame(admin_window)
        add_frame.pack(pady=10)
        add_question_label = tk.Label(add_frame, text="Question:")
        add_question_label.grid(row=0, column=0)
        add_question_entry = tk.Entry(add_frame, width=50)
        add_question_entry.grid(row=0, column=1)
        add_answer_label = tk.Label(add_frame, text="Answer:")
        add_answer_label.grid(row=1, column=0)
        add_answer_entry = tk.Entry(add_frame, width=50)
        add_answer_entry.grid(row=1, column=1)
        add_button = tk.Button(add_frame, text="Add", command=lambda: add_data(
            add_question_entry.get(), add_answer_entry.get()))
        add_button.grid(row=2, column=1)

        # Update data form
        update_frame = tk.Frame(admin_window)
        update_frame.pack(pady=10)
        update_id_label = tk.Label(update_frame, text="ID:")
        update_id_label.grid(row=0, column=0)
        update_id_entry = tk.Entry(update_frame, width=50)
        update_id_entry.grid(row=0, column=1)
        update_question_label = tk.Label(update_frame, text="Question:")
        update_question_label.grid(row=1, column=0)
        update_question_entry = tk.Entry(update_frame, width=50)
        update_question_entry.grid(row=1, column=1)
        update_answer_label = tk.Label(update_frame, text="Answer:")
        update_answer_label.grid(row=2, column=0)
        update_answer_entry = tk.Entry(update_frame, width=50)
        update_answer_entry.grid(row=2, column=1)
        update_button = tk.Button(update_frame, text="Update", command=lambda: update_data(
            update_id_entry.get(), update_question_entry.get(), update_answer_entry.get()))
        update_button.grid(row=3, column=1)

    else:
        error_label.config(text="Invalid username or password. Try again.")


def clear_chat():
    chat_history.delete('1.0', END)
    bot_response.delete(0, END)

# =========================================================================================================#
# Main chatbot interface


root = Tk()

root.title('SRM Institute of Science and Technology')
root.iconbitmap('C:\\Users\\pawan\\Desktop\\chatbot for student\\srm logo.ico')

root.maxsize(700, 700)
root.minsize(700, 700)

root.configure(background='#0096DC')
img = Image.open('Srmseal.png')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

text_label = Label(root, text='SRM AI', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))

user_input = Entry(root, width=50)
user_input.pack(ipady=6, pady=(1, 15))

bot_response = Entry(root, width=50)
bot_response.pack(ipady=6, pady=(1, 15))

btn_send = Button(root, text='Send', command=Enter_pressed, width=10, height=2)
btn_send.place(relx=0.57, rely=0.95, anchor='s')

btn_clear = Button(root, text='Clear', command=clear_chat, width=10, height=2)
btn_clear.place(relx=0.43, rely=0.95, anchor='s')


chat_history = Text(root)
chat_history.pack()

# binds the Enter key to the Enter_pressed function
root.bind('<Return>', Enter_pressed)

# ================================================================================================================#


# admin window
root = tk.Tk()
root.title("SRM AI")
root.iconbitmap('C:\\Users\\pawan\\Desktop\\chatbot for student\\srm logo.ico')

root.maxsize(700, 700)
root.minsize(700, 700)

root.configure(background='#0096DC')
text_label = Label(root, text='SRM ADMIN LOGIN', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))

# Create admin login form
admin_login_frame = tk.Frame(root)
admin_login_frame.pack()
admin_username_label = tk.Label(admin_login_frame, text="Username:")
admin_username_label.grid(row=0, column=0)
admin_username = tk.Entry(admin_login_frame, width=50)
admin_username.grid(row=0, column=1)
admin_password_label = tk.Label(admin_login_frame, text="Password:")
admin_password_label.grid(row=1, column=0)
admin_password = tk.Entry(admin_login_frame, width=50, show="*")
admin_password.grid(row=1, column=1)
admin_button = tk.Button(
    admin_login_frame, text="Admin Login", command=handle_admin_command)
admin_button.grid(row=2, column=1)
error_label = tk.Label(admin_login_frame, text="")
error_label.grid(row=3, column=1)


# =================================================================================================================#


root.title('SRM Institute of Science and Technology')
root.iconbitmap('C:\\Users\\pawan\\Desktop\\chatbot for student\\srm logo.ico')

root.configure(background='#0096DC')

# Define functions to connect to websites


def connect_to_attendance():
    webbrowser.open("https://q.srmcheck.me/attendance")


def connect_to_results():
    webbrowser.open("https://q.srmcheck.me/marks")


def connect_to_events():
    webbrowser.open("https://academia.srmist.edu.in/#Academic_Reports")

# Add buttons for attendance, results, and events


root.maxsize(500, 500)
root.minsize(500, 500)

btn_send = Button(root, text='attaindance',
                  command=connect_to_attendance, width=15, height=3)
btn_send.place(relx=0.20, rely=0.95, anchor='s')

btn_clear = Button(root, text='Result',
                   command=connect_to_results, width=15, height=3)
btn_clear.place(relx=0.50, rely=0.95, anchor='s')

btn_clear = Button(root, text='events',
                   command=connect_to_events, width=15, height=3)
btn_clear.place(relx=0.80, rely=0.95, anchor='s')


# Start main loop
root.mainloop()
