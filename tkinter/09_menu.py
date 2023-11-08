### Menu ###

from tkinter import Tk, Label, Menu

window = Tk()
window.geometry('600x400')

main_menu = Menu(window)
window.config(menu=main_menu)

files = Menu(main_menu, tearoff=0)
files.add_command(label='New Text File')
files.add_command(label='New File')
files.add_command(label='New Window')
files.add_separator()
files.add_command(label='Open File')
files.add_command(label='Open Folder')
files.add_command(label='Open Workspace From File')
files.add_separator()
files.add_command(label='Salir', command=files.quit)

edit = Menu(main_menu, tearoff=0)
edit.add_command(label='Undo')
edit.add_command(label='Redo')
edit.add_separator()
edit.add_command(label='Cut')
edit.add_command(label='Copy')
edit.add_command(label='Paste')

selection = Menu(main_menu, tearoff=0)
selection.add_command(label='Select All')
selection.add_command(label='Expand Selection')
selection.add_command(label='Shrink Selection')
selection.add_separator()
selection.add_command(label='Copy Line Up')
selection.add_command(label='Copy Line Down')

main_menu.add_cascade(label="Files", menu=files)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="Selection", menu=selection)
main_menu.add_cascade(label="View")
main_menu.add_cascade(label="Go")
main_menu.add_cascade(label="Run")
main_menu.add_cascade(label="Termina")
main_menu.add_cascade(label="Help")


window.mainloop()