import tkinter as tk 
from tkinter import ttk

def boton_presionado():
    print("El boton fue presionado")
    boton.config(text="Fue presionado el boton")


ventana_principal = tk.Tk()
ventana_principal.title("Segunda Ventana")

boton = ttk.Button(ventana_principal, text="Presione aquí", command=boton_presionado )
boton.place(x=50, y=10)


ventana_principal.mainloop()