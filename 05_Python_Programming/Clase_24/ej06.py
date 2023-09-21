import tkinter as tk
from tkinter import ttk

def btn_presionado():
    print("Ha presionado el boton "+cbx.get())
    print(lista.get())
   #cbx.insert(0, "Gracias!")
   #cbx.delete(0, 20) 
    cbx.delete(0, tk.END) 
    

window = tk.Tk()
window.title("Bienvenidos a Tkinter") 
window.config(width=300, height=200)

lbl = ttk.Label(window, text="Ingrese un número:") # , font=("Arial Bold", 50)
lbl.place(x=10, y=10)

cbx = ttk.Entry(window)
cbx.place(x=130, y=10)

lista = ttk.Combobox(window, values = ["Paris", "Madrid", "Buenos Aires", "Roma", "New York"])
lista.place(x=130, y=50)

btn = ttk.Button(window, text="Presione aqui", command=btn_presionado)
btn.place(x=130, y=150)

window.mainloop()