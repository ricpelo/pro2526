"""
Una calculadora sencilla.
"""

import tkinter as tk
from tkinter import messagebox


class OperatorError(ValueError):
    pass


class Aplicacion(tk.Tk):
    """La calculadora."""

    def __init__(self) -> None:
        super().__init__()

        self.title("Calculadora")
        self.option_add("*Font", ("Arial", 24))

        self.__op1_label = tk.Label(self, text="Primer operando:", bg="white")
        self.__op1_label.pack()

        self.__op1 = tk.Entry(self)
        self.__op1.pack(fill=tk.X, expand=False)

        self.__op2_label = tk.Label(self, text="Segundo operando:")
        self.__op2_label.pack()

        self.__op2 = tk.Entry(self)
        self.__op2.pack()

        self.__op_label = tk.Label(self, text="Operador (+, -, *, /):")
        self.__op_label.pack()

        self.__op = tk.Entry(self)
        self.__op.pack()

        self.__boton = tk.Button(self, text="Calcular", command=self.calcular)
        self.__boton.pack()

        self.bind("<Return>", self.calcular)
        self.bind("<KP_Enter>", self.calcular)

        self.__res_label = tk.Label(self, text="Resultado:")
        self.__res_label.pack()

        self.__res = tk.Label(self, text="")
        self.__res.pack()

        self.__cerrar = tk.Button(self, text="Cerrar", command=self.quit)
        self.__cerrar.pack()


    def calcular(self, event=None) -> None:
        """Calcula el resultado y lo mete en la etiqueta correspondiente."""
        try:
            op1 = float(self.__op1.get())
            op2 = float(self.__op2.get())
            op = self.__op.get()
            match op:
                case '+': res = op1 + op2
                case '-': res = op1 - op2
                case '*': res = op1 * op2
                case '/': res = op1 / op2
                case _: raise OperatorError()
            self.__res["text"] = res
        except OperatorError:
            messagebox.showerror('Error', 'Operación incorrecta.')
        except ValueError:
            messagebox.showerror('Error', 'Operando incorrecto.')
        except ZeroDivisionError:
            messagebox.showerror('Error', 'No se puede dividir entre cero.')


app = Aplicacion()
app.mainloop()
