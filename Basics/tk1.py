from tkinter import *
from PIL import ImageTk, Image

def login():
    email = email_entry.get()
    password = password_entry.get()
    if email and password:
        root.destroy()
        welcome_window = Tk()
        welcome_window.title("Welcome")
        welcome_window.geometry('400x200')
        welcome_window.configure(bg='#00704A')
        welcome_label = Label(welcome_window, text=f"Welcome, {email}!", 
                              font=('Verdana', 20, 'bold'), bg='#000000', fg='white')
        welcome_label.pack(pady=100)
        welcome_window.mainloop()
    else:
        error_label.config(text="Please enter email and password!")

root = Tk()
root.title("Student Form")
root.geometry('500x500+0+0')
root.configure(background='#00704A')

# Image
img = Image.open('ch7.jpg')
resize_img = img.resize((100, 70))
img = ImageTk.PhotoImage(resize_img)
img_label = Label(root, image=img)
img_label.pack(pady=10, padx=20)

# Text label
text_label = Label(root, text="Current WWE Sucks", font=('Cursive', 18, 'bold'), 
                   bg='#000000', fg='white')
text_label.pack(pady=10, padx=20)

# Email
email_label = Label(root, text="Email", font=('Arial', 18, 'bold'), bg='#00704A', fg='white')
email_label.pack(pady=(20, 5))
email_entry = Entry(root, font=('Arial', 18, 'bold'), fg='white', bg='grey')
email_entry.pack(pady=(5, 10))

# Password
password_label = Label(root, text="Password", font=('Arial', 18, 'bold'), bg='#00704A', fg='white')
password_label.pack(pady=(20, 5))
password_entry = Entry(root, font=('Arial', 18, 'bold'), fg='white', bg='grey', show='*')
password_entry.pack(pady=(5, 10))

# Error label
error_label = Label(root, text="", font=('Arial', 12, 'bold'), bg='#00704A', fg='red')
error_label.pack()

# Login button
login_btn = Button(root, text="Login", font=('Arial', 18, 'bold'), bg='#00704A', fg='white', command=login)
login_btn.pack(pady=(5, 10))

root.mainloop()