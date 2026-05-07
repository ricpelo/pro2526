"""
Una calculadora sencilla.
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class OperatorError(ValueError):
    pass


class Aplicacion(tk.Tk):
    """La calculadora."""

    def __init__(self) -> None:
        super().__init__()

        self.title("Calculadora")
        self.option_add("*Font", ("Arial", 24))
        ttk.Style().configure("TRadiobutton", font=("Arial", 24))

        self.__op1_label = tk.Label(self, text="Primer operando:")
        self.__op1_label.grid(row=0, column=0)

        self.__op1 = tk.Entry(self)
        self.__op1.grid(row=0, column=1)

        self.__op2_label = tk.Label(self, text="Segundo operando:")
        self.__op2_label.grid(row=1, column=0)

        self.__op2 = tk.Entry(self)
        self.__op2.grid(row=1, column=1)

        self.__op_label = tk.Label(self, text="Operador:")
        self.__op_label.grid(row=2, column=0)

        # self.__op = tk.Entry(self)
        # self.__op.pack()

        self.__operadores = tk.Frame(self)
        self.__operadores.grid(row=2, column=1)

        self.__op = tk.StringVar()
        self.__rb_add = ttk.Radiobutton(self.__operadores, text="+", variable=self.__op, value="+")
        self.__rb_sub = ttk.Radiobutton(self.__operadores, text="-", variable=self.__op, value="-")
        self.__rb_mul = ttk.Radiobutton(self.__operadores, text="*", variable=self.__op, value="*")
        self.__rb_div = ttk.Radiobutton(self.__operadores, text="/", variable=self.__op, value="/")
        self.__rb_add.grid(row=0, column=0, padx=10)
        self.__rb_sub.grid(row=0, column=1, padx=10)
        self.__rb_mul.grid(row=0, column=2, padx=10)
        self.__rb_div.grid(row=0, column=3, padx=10)
        self.__op.set('+')

        self.__res_label = tk.Label(self, text="Resultado:")
        self.__res_label.grid(row=3, column=0)

        self.__res = tk.Label(self, text="")
        self.__res.grid(row=3, column=1)

        self.__boton = tk.Button(self, text="Calcular", command=self.calcular)
        self.__boton.grid(row=4, column=0)

        self.bind("<Return>", self.calcular)
        self.bind("<KP_Enter>", self.calcular)

        self.__cerrar = tk.Button(self, text="Cerrar", command=self.quit)
        self.__cerrar.grid(row=4, column=1)


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
