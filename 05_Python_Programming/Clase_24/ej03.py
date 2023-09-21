import tkinter as tk 
from tkinter import ttk 

def btn_presionado():
    print("Se escribió el numero:", cbx.get())
    cbx.delete(0, tk.END)

window = tk.Tk()
window.title("Bienvenidos a Tk")
window.config(width=300, height=200)

lbl = ttk.Label(window, text="Ingrese un número:")
lbl.place(x=10, y=10)

cbx = ttk.Entry(window)
cbx.place(x=130, y=10)

btn = ttk.Button(window, text="Presione aquí", command=btn_presionado)
btn.place(x=130, y=50)

window.mainloop()