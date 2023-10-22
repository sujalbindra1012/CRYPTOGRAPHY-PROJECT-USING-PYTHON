from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet


def encrypt():
    password = code.get()
    message = text1.get(1.0, END).encode()

    if password == "1012":
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_message = cipher_suite.encrypt(message).decode()

        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        Label(screen1, text="ENCRYPT", font="arial",
              fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Robote 10", bg="white",
                     relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypted_message)

    elif password == "":
        messagebox.showerror("Encryption", "Input password")

    else:
        messagebox.showerror("Encryption", "Incorrect password")


def decrypt():
    password = code.get()
    message = text1.get(1.0, END).encode()

    if password == "0511":
        try:
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            decrypted_message = cipher_suite.decrypt(message).decode()

            screen2 = Toplevel(screen)
            screen2.title("Decryption")
            screen2.geometry("400x200")
            screen2.configure(bg="#00bd56")

            Label(screen2, text="DECRYPT", font="arial",
                  fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = Text(screen2, font="Robote 10", bg="white",
                         relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, decrypted_message)

        except:
            messagebox.showerror("Decryption", "Invalid or corrupted data")

    elif password == "":
        messagebox.showerror("Decryption", "Input password")

    else:
        messagebox.showerror("Decryption", "Incorrect password")


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Crypto")

    Label(text="Enter text for encryption and decryption",
          fg="black", font=("calibri", 13)).place(x=1)
    text1 = Text(font="Robote 20", bg="white", fg="red",
                 relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption",
          fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=(
        "arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833",
           fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place
