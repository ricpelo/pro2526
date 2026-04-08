import tkinter as tk

class Aplicacion(tk.Tk):
    """La clase que representa la aplicación."""

    def __init__(self):
        super().__init__()
        # self.geometry("800x600")
        self.title("Esto es una prueba")
        self.option_add("*Font", ("Arial", 32))
        
        self.__texto = tk.Label(self, text="¡Hola!")
        self.__texto.pack()
        
        self.__entrada = tk.Entry(self)
        self.__entrada.pack()
        
        self.__boton = tk.Button(
            self,
            text="¡Púlsame!",
            command=self.__cambiar_texto
        )
        self.__boton.pack()

        self.__salida = tk.Label(self, text="", fg="green")
        self.__salida.pack()
        
        self.bind("<Return>", self.__cambiar_texto)     # Intro
        self.bind("<KP_Enter>", self.__cambiar_texto)   # Intro numérico
        
        
    def __cambiar_texto(self, event=None):
        self.__salida["text"] = self.__entrada.get()
        # self.salida.config(text=self.entrada.get())
        if self.__texto["text"] == "¡Hola!":
            self.__texto["text"] = "¡Adiós!"
        else:
            self.__texto["text"] = "¡Hola!"


app = Aplicacion()
app.mainloop()