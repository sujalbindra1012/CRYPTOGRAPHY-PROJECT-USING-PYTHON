from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet


def decrypt():
    password = code.get()

    if password == "0511":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        encrypted_message = message.encode("utf-8")

        cipher_suite = Fernet(password.encode("utf-8"))
        decrypted_message = cipher_suite.decrypt(
            encrypted_message).decode("utf-8")

        Label(screen2, text="DECRYPT", font="arial",
              fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="white",
                     relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted_message)

    elif password == "":
        messagebox.showerror("Decryption", "Input password")

    else:
        messagebox.showerror("Decryption", "Incorrect password")


def encrypt():
    password = code.get()

    if password == "1012":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        plaintext_message = message.encode("utf-8")

        cipher_suite = Fernet(password.encode("utf-8"))
        encrypted_message = cipher_suite.encrypt(
            plaintext_message).decode("utf-8")

        Label(screen1, text="ENCRYPT", font="arial",
              fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white",
                     relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted_message)

    elif password == "":
        messagebox.showerror("Encryption", "Input password")

    else:
        messagebox.showerror("Encryption", "Incorrect password")


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Crypto")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for encryption and decryption",
          fg="black", font=("calbri", 13)).place(x=1)
    text1 = Text(font="Roboto 20", bg="white", fg="red",
                 relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption",
          fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=(
        "arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833",
           fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56",
           fg="white", bd=0, command=decrypt).place(x=200, y=250)

    Button(text="RESET", height="2", width=50, bg="#1089ff",
           fg="white", bd=0, command=reset).place(x=10, y=300)
    screen.mainloop()


main_screen()
