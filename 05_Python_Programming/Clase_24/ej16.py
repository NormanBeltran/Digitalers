from tkinter import *
ventana = Tk()

for r in range(0, 5):
    for c in range(0, 5):
        celda = Entry(ventana, width=10)
        celda.grid(padx=1, pady=1, row=r, column=c)
        celda.insert(0, '({}, {})'.format(r, c))

ventana.mainloop()