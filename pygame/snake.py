from tkinter import *

root = Tk()

mylabel = Label(root, text="HELLO WORLD!", foreground="White", background="#34A2FE", border="10")
btn = Button(root, text="CLICK ME!", foreground="green", bg="purple", border="20")
nameLabel = Label(root, text="Name: ")
nameEntry = Entry(root)
mylabel.pack()
btn.pack()
nameLabel.pack()
nameEntry.pack()
nameEntry.insert(0, "python")
a = nameEntry.get()
txt = Text()
txt.pack()
b = txt.get("1.0",END)
root.mainloop()
print(b)
