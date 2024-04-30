from tkinter import *
import string
import random as rd
import messagebox

win = Tk()
win.title("Generate Password") 
win.size = "500x500"
win.resizable(False, False)

lett_dig_punc = string.ascii_letters + string.digits + string.punctuation

size = IntVar(win, "", "size")
resultat  = StringVar(win, "")
isChecked = StringVar(win, "Garde Number")
lsBox = list()


def generate():
    ls_generations = ""
    try:
        if size.get() < 30: taill_password = size.get()
        else: taill_password = 29
    except:
        taill_password = 8

    size.set("") if isChecked.get() == "Garde Number" else None

    for i in range(taill_password):
        selection = rd.randint(0, len(lett_dig_punc) - 1)
        ls_generations += lett_dig_punc[selection]

    ls.insert(0, ls_generations)
    resultat.set(ls_generations)

def clearList():
    if messagebox.askyesno("confirmation", "are you sure"):
        ls.delete(0, END)

def toggleBox():
    isChecked.set("Garde Number") if isChecked.get() == "Garde Number " else isChecked.set("Garde Number ")
        

def cancel():
    win.destroy()


Label(win, text="Password Generated").grid(row = 3, column= 0)
Entry(win, textvariable=resultat, background="lightblue", width=30, font="arial 12").grid(padx = 20, pady=10, column=1, row=3)

Button(win, text="Generate", bg="lightgreen", fg="darkblue", command=generate, width=20, activebackground="lightblue").grid(column=1, row=0)
Button(win, text="Cancel", bg="lightpink", fg="darkblue", command=cancel, width=20, activebackground="lightblue").grid(column=1, row=1)

Label(win, text="Size").grid(row = 0, column= 0)
Entry(win, textvariable=size, background="lightblue", name="size", width=10).grid(padx = 20, pady=10, column=0, row=1)


chk = Checkbutton(win, text="Garde Number", textvariable=isChecked, command=toggleBox).grid(row=2, column=0)

ls = Listbox(win, width=50, height=5, listvariable=lsBox)
ls.grid(row=4, column=0, columnspan=3)
Button(text="Clear", command=clearList, background="lightpink", activebackground="lightblue", bd=1, width=13, foreground="darkblue").grid(row=5, columnspan=4, pady=2, ipady=3)

win.mainloop()