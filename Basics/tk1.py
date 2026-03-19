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
        welcome_window.configure(bg='black')
        
        welcome_label = Label(
            welcome_window, 
            text=f"Welcome, {email}!", 
            font=('Verdana', 20, 'bold'), 
            bg='black', 
            fg='red'
        )
        welcome_label.pack(expand=True)
        
        welcome_window.mainloop()
    else:
        error_label.config(text="Please enter email and password!")

root = Tk()
root.title("Death Form")
root.geometry('500x500+0+0')
root.configure(bg='black')

img = Image.open('ch7.jpg')
resize_img = img.resize((100, 70))
img = ImageTk.PhotoImage(resize_img)
img_label = Label(root, image=img, bg='black')
img_label.pack(pady=10)

text_label = Label(
    root, text="Current WWE Sucks", 
    font=('Impact', 22, 'bold'), 
    bg='black', fg='red'
)
text_label.pack(pady=10)

email_label = Label(root, text="Email", font=('Arial', 16, 'bold'), bg='black', fg='white')
email_label.pack(pady=(20, 5))
email_entry = Entry(root, font=('Arial', 16, 'bold'), fg='black', bg='white')
email_entry.pack(pady=(5, 10))

password_label = Label(root, text="Password", font=('Arial', 16, 'bold'), bg='black', fg='white')
password_label.pack(pady=(20, 5))
password_entry = Entry(root, font=('Arial', 16, 'bold'), fg='black', bg='white', show='*')
password_entry.pack(pady=(5, 10))

error_label = Label(root, text="", font=('Arial', 12, 'bold'), bg='black', fg='red')
error_label.pack()

login_btn = Button(root, text="Login", font=('Arial', 16, 'bold'), bg='red', fg='white', command=login)
login_btn.pack(pady=(5, 10))

root.mainloop()