import tkinter as tk
from tkinter import messagebox


def sumar ():
    Valor_a= int(a.get())
    Valor_b= int(b.get())
    resultado = Valor_a + Valor_b
    label_resultado.config(text=f"{resultado}") 


def restar ():
    return a - b

def multiplicar (a, b):
    return a * b




#crear ventana 
ventana = tk.Tk()
ventana.title("Practicando a usar tkinter")
ventana.geometry("720x680")

tk.Label(ventana, text="Calculadora").pack(pady=5, padx=5, fill="x")
tk.Label(ventana, text="Numero 1").pack(pady=5)
a= tk.Entry(ventana)
a.pack(pady=5)
tk.Label(ventana, text="Numero 2").pack(pady=5)
b= tk.Entry(ventana)
b.pack(pady=5)

tk.Button( ventana, text="Sumar", command = sumar).pack(pady=5)
tk.Button( ventana, text="multiplicar", command = multiplicar).pack(pady=5)
tk.Button( ventana, text="restar", command = restar).pack(pady=5)

label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

#ejecutar la aventana o aplicacion


ventana.mainloop()



