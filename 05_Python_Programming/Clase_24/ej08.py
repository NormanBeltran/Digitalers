# Radio button
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
variable = tk.IntVar()

def prueba():
    print("Se ha elegido la opcion", variable.get())

radiobutton1 = tk.Radiobutton(text="Opcion 1", variable=variable, value=1, command=prueba)
radiobutton2 = tk.Radiobutton(text="Opcion 2", variable=variable, value=2, command=prueba)
radiobutton3 = tk.Radiobutton(text="Opcion 3", variable=variable, value=3, command=prueba)

radiobutton1.place(x=10, y=10)
radiobutton2.place(x=10, y=30)
radiobutton3.place(x=10, y=50)

root.mainloop()