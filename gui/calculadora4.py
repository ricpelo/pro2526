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
        # ttk.Style().configure("TCombobox", font=("Arial", 48))

        self.grid_columnconfigure(0, weight=1) # Expande columna 1
        self.grid_columnconfigure(1, weight=1) # Expande columna 1
        self.resizable(True, False)

        self.__op1_label = tk.Label(self, text="Primer operando:")
        self.__op1_label.grid(row=0, column=0, sticky="e", padx=(10, 0), pady=10)

        self.__op1 = tk.Entry(self, width=10)
        self.__op1.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        self.__op2_label = tk.Label(self, text="Segundo operando:")
        self.__op2_label.grid(row=1, column=0, sticky="e", padx=(10, 0), pady=10)

        self.__op2 = tk.Entry(self, width=10)
        self.__op2.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

        self.__op_label = tk.Label(self, text="Operador:")
        self.__op_label.grid(row=2, column=0, sticky="e", padx=(10, 0), pady=10)

        # self.__op = tk.Entry(self)
        # self.__op.pack()

        self.__op = ttk.Combobox(self, values=["+", "-", "*", "/"], state="readonly", width=3)
        self.__op.current(0)
        self.__op.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        self.__res_label = tk.Label(self, text="Resultado:")
        self.__res_label.grid(row=3, column=0, sticky="e", padx=(10, 0), pady=10)

        self.__res = tk.Label(self, text="")
        self.__res.grid(row=3, column=1, sticky="w", padx=10, pady=10)

        self.__botones = tk.Frame(self)
        self.__botones.grid(row=4, column=0, columnspan=2, pady=10)

        self.__boton = tk.Button(self.__botones, text="Calcular", command=self.calcular)
        self.__boton.pack(side=tk.LEFT, padx=5)

        self.bind("<Return>", self.calcular)
        self.bind("<KP_Enter>", self.calcular)

        self.__cerrar = tk.Button(self.__botones, text="Cerrar", command=self.quit)
        self.__cerrar.pack(side=tk.LEFT, padx=5)


    def calcular(self, event=None) -> None:
        """Calcula el resultado y lo mete en la etiqueta correspondiente."""
        try:
            op1 = float(self.__op1.get())
            op2 = float(self.__op2.get())
            op = self.__op.get()
            print(op)
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
