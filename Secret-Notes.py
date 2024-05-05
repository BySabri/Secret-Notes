import tkinter
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
def savebuttonfunc():
    title = titleentry.get()
    note = secretEntry.get("1.0", "end")
    key = keyEntry.get()

    if len(title) == 0 or len(note) == 0 or len(key) == 0:
        messagebox.showerror(title="Error", message="Fill All Boxes")
    else:
        messageencrypted = encode(key, note)
        try:
            with open("../mydata.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{messageencrypted}")
        except FileNotFoundError:
            with open("../mydata.txt", "w") as data_file:
                data_file.write(f"\n{title}\n{messageencrypted}")
        finally:
            titleentry.delete(0, "end")
            secretEntry.delete(1.0, "end")
            keyEntry.delete(0, "end")

def decryptnotes():
    note_encrypted = secretEntry.get("1.0", "end")
    key = keyEntry.get()

    if len(note_encrypted) == 0 or len(key) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(key,note_encrypted)
            secretEntry.delete("1.0", "end")
            secretEntry.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")


window = tkinter.Tk()
window.title("Secret Notes")
window.config(bg="black")
window.minsize(width=500, height=400)
window_width = 500
window_height = 400

center_window(window, window_width, window_height)


titlelabel = tkinter.Label()
titlelabel.config(text="Enter Your Title:", fg="white", bg="black")
titlelabel.pack()

titleentry = tkinter.Entry()
titleentry.config(width=30, bg="white")
titleentry.pack()

secretlabel = tkinter.Label()
secretlabel.config(text="Enter Your Note:", fg="white", bg="black")
secretlabel.pack()

secretEntry = tkinter.Text()
secretEntry.config(width=23, height=10, bg="white")
secretEntry.pack()

keyLabel = tkinter.Label()
keyLabel.config(text="Enter Your Key:", fg="white", bg="black")
keyLabel.pack()

keyEntry = tkinter.Entry()
keyEntry.config(width=30, bg="white")
keyEntry.pack()

saveButton = tkinter.Button()
saveButton.config(text="Save and Encrypt", width=15, bg="white", command=savebuttonfunc)
saveButton.place(x=195, y=280)

decryptButton = tkinter.Button()
decryptButton.config(text="Decrypt", width=15, bg="green", fg="white", command=decryptnotes)
decryptButton.place(x=195, y=320)


window.mainloop()