import base64
from tkinter import *

root = Tk()


root.title("Tencoder16")




e1 = Entry(root, borderwidth=5, width=200)
e1.insert(0, "Enter a text to encode")
def Encode():
    text = e1.get()
    print(text)
    encoded = base64.b16encode(text.encode('ascii'))
    e1.delete(0, END)
    e1.insert(0, encoded)
    print(encoded)


b1 = Button(root, text="Encode", command=Encode)


e1.grid(row=0, column=0)
b1.grid(row=1, column=0)

e2 = Entry(root, borderwidth=5, width=200)
e2.insert(0, "Enter a text to decode")
def Decode():
    text = e2.get()
    text = text.encode('ascii')
    print(text)
    decoded = base64.b16decode(text.decode('ascii'))
    e2.delete(0, END)
    e2.insert(0, decoded)
    print(decoded)

b2 = Button(root, text="Decode", command=Decode)

e2.grid(row=2, column=0)
b2.grid(row=3, column=0)

t = Label(root, text="Tencoder16 encodes text to bytes using base16, for other methods of encoding, please download a different version of Tencoder", fg="green")
t.grid(row=4, column=0)
t1 = Label(root, text="Made by Doges 2022", fg="green")
t1.grid(row=5, column=0)

root.mainloop()




