import tkinter as tk
from tkinter import messagebox








#crear ventana 
ventana = tk.Tk()
ventana.title("Practicando a usar tkinter")
ventana.geometry("720x680")

tk.Label(ventana, text="Nombre del estudiante:").pack(pady=5, padx=5, fill="x")


#ejecutar la aventana o aplicacion


ventana.mainloop()