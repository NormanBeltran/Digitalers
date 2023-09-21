# Imagen
import tkinter as tk

ventana=tk.Tk()
canvas=tk.Canvas(ventana, width=700, height=600, background="black")
canvas.grid(column=0, row=0)
archi=tk.PhotoImage(file="dis.gif")
canvas.create_image(30, 30, image=archi, anchor="nw")

ventana.mainloop()