import tkinter as tk

def imprimir_seleccion():
    for i in lista.curselection():
     print(i)

ventana=tk.Tk()
ventana.config(width=600, height=500)

lista = tk.Listbox(selectmode=tk.EXTENDED, selectforeground="#ffffff", selectbackground="#3335FF", selectborderwidth=5)
lista.insert(0, "Python", "C", "C++", "Java")
lista.place(x=10, y=10)

boton = tk.Button(text="Imprimir seleccion", command=imprimir_seleccion)
boton.place(x=160, y=10)

ventana.mainloop()