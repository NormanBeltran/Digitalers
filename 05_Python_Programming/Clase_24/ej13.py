from tkinter import *

fields = 'Name', 'Job', 'Pay', 'Play', 'Save'

def fetch(entries):
    for entry in entries:
        print('Input => "%s"' % entry.get())        # get text

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)                           # make a new row
        lab = Label(row, width=5, text=field)       # add label, entry
        ent = Entry(row)
        row.pack(side=TOP, fill=X)                  # pack row on top
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)    # grow horizontal
        entries.append(ent)
    return entries

def show(entries, popup):
    fetch(entries)                  # must fetch before window destroyed!
    popup.destroy()                 # fails with msgs if stmt order is reversed

def ask():
    popup = Toplevel()              # show form in modal dialog window
    ents = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda: show(ents, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()             # wait for destroy here

root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()