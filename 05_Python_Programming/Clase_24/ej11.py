# Menu
import tkinter as tk
from tkinter import ttk


def saludar():
    print("Ingreso en la funcion saludar()")
    saludo = "Hola " + caja.get()
    etiqueta1.config(text=saludo)

ventana = tk.Tk()
ventana.title("Empresa SA")
ventana.config(width=600, height=500)

etiqueta = tk.Label(text="Ingrese su nombre")
etiqueta.place(x=20,y=20)

caja = tk.Entry()
caja.place(x=150,y=20, width=200, height=20)

boton = tk.Button(text="Saludo", command=saludar)
boton.place(x=150, y=50, width=100, height=20)

etiqueta1 = tk.Label(text="")
etiqueta1.place(x=60,y=80)
etiqueta1.config(
                #fg="blue",    # Foreground
                #bg="grey",   # Background
                 font=("Arial",24)) 

#____________________ Menu
menubar = tk.Menu(ventana)
ventana.config(menu=menubar)  

filemenu = tk.Menu(menubar, tearoff=0) # 
editmenu = tk.Menu(menubar, tearoff=0) # 
helpmenu = tk.Menu(menubar, tearoff=0) # 

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# FileMenu
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=ventana.quit)

# EditMenu
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

# HelpMenu
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

ventana.mainloop()