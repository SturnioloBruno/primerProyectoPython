from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos")

CRUDMenu=Menu(barraMenu, tearoff=0)
CRUDMenu.add_command(label="Crear")
CRUDMenu.add_command(label="Leer")
CRUDMenu.add_command(label="Actualizar")
CRUDMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=CRUDMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


root.mainloop()