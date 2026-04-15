import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tareas pendientes')
        self.option_add('*Font', ('Arial', 24))

        self.__frame_izq = tk.Frame(self)
        self.__frame_izq.pack(side=tk.LEFT)

        self.__label_izq = tk.Label(self.__frame_izq, text='Tarea a agregar:')
        self.__label_izq.pack()

        self.__entry = tk.Entry(self.__frame_izq)
        self.__entry.pack()

        self.__button = tk.Button(self.__frame_izq, text='Agregar', command=self.agregar)
        self.__button.pack()

        self.__cambiar = tk.Button(self.__frame_izq, text='Cambiar', command=self.cambiar)
        self.__cambiar.pack()

        self.__quitar = tk.Button(self.__frame_izq, text='Quitar', command=self.quitar)
        self.__quitar.pack()

        self.__guardar = tk.Button(self.__frame_izq, text='Guardar', command=self.guardar)
        self.__guardar.pack()

        self.__frame_der = tk.Frame(self)
        self.__frame_der.pack(side=tk.LEFT)

        self.__label_der = tk.Label(self.__frame_der, text='Tareas pendientes:')
        self.__label_der.pack()

        self.__listbox = tk.Listbox(self.__frame_der)
        self.__listbox.pack()

        self.__listbox.bind('<<ListboxSelect>>', self.seleccionar)


    def seleccionar(self, _=None) -> None:
        sel = self.__listbox.curselection()
        if len(sel) > 0:
            indice = sel[0]
            texto = self.__listbox.get(indice)
            self.__entry.delete(0, tk.END)
            self.__entry.insert(0, texto)


    def cambiar(self, _=None) -> None:
        sel = self.__listbox.curselection()
        texto = self.__entry.get()
        if len(sel) > 0 and len(texto) > 0:
            indice = sel[0]
            self.__listbox.delete(indice)
            self.__listbox.insert(indice, texto)
            self.__entry.delete(0, tk.END)


    def quitar(self, _=None) -> None:
        sel = self.__listbox.curselection()
        if len(sel) > 0:
            indice = sel[0]
            self.__listbox.delete(indice)


    def agregar(self, _=None) -> None:
        t = self.__entry.get().strip()
        if len(t) > 0:
            self.__listbox.insert(tk.END, t)
            self.__entry.delete(0, tk.END)


    def guardar(self) -> None:
        with open('archivo.txt', 'w') as f:
            f.writelines(l + '\n' for l in self.__listbox.get(0, tk.END))


app = Aplicacion()
app.mainloop()
