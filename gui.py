import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("320x200")
ventana.title("Mi primera aplicación Tkinter")

# Añadir un botón
boton = tk.Button(ventana, text="Haz clic aquí")
boton.pack()

# Iniciar el bucle principal
ventana.mainloop()