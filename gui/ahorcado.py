"""
El juego del ahorcado.
"""

import tkinter as tk
from tkinter import messagebox
import random


class Aplicacion(tk.Tk):
    """La clase principal del juego del ahorcado."""

    NUM_INTENTOS = 10

    def __init__(self):
        super().__init__()

        self.reiniciar()

        self.title('El juego del ahorcado')
        self.option_add('*Font', ('Mono', 20))

        self.__frame = tk.Frame(self)
        self.__frame.pack()

        self.__label_entrada = tk.Label(self.__frame, text='Letra a probar:')
        self.__label_entrada.pack(side=tk.LEFT)

        self.__entrada = tk.Entry(self.__frame, width=2)
        self.__entrada.pack(side=tk.LEFT)

        self.__probar = tk.Button(self.__frame, text='Probar', command=self.probar)
        self.__probar.pack(side=tk.LEFT, padx=(10, 0))

        self.__adivinado = tk.Label(self, text=self.texto_adivinado())
        self.__adivinado.pack()

        self.__label_intentos = tk.Label(self, text=f'Te quedan {self.__intentos} intentos')
        self.__label_intentos.pack()

        self.__label_erroneas = tk.Label(self, text='')
        self.__label_erroneas.pack()

        self.__salir = tk.Button(self, text='Salir', command=self.quit)
        self.__salir.pack()

        self.bind('<Return>', self.probar)
        self.bind('<Escape>', lambda _: self.quit())


    def reiniciar(self) -> None:
        """Inicializa el juego."""
        self.__adivinadas: set[str] = set()
        self.__erroneas: set[str] = set()
        self.__intentos = Aplicacion.NUM_INTENTOS

        with open('/usr/share/dict/words', encoding='utf-8') as f:
            palabras = f.readlines()

        quitar_acentos = str.maketrans({'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'})
        self.__palabra_a_adivinar = random.choice(palabras) \
            .strip() \
            .upper() \
            .translate(quitar_acentos)
        print(self.__palabra_a_adivinar)


    def texto_adivinado(self) -> str:
        """Devuelve el texto que tiene que mostrarse, con letras y _."""
        return ' '.join(c if c in self.__adivinadas else '_' for c in self.__palabra_a_adivinar)
        """
        res = []
        for c in self.__palabra_a_adivinar:
            if c in self.__adivinadas:
                res.append(c)
            else:
                res.append('_')
        return ' '.join(res)
        """


    def comprobar_acierto(self) -> bool:
        """Devuelve True si el jugador ha adivinado la palabra."""
        return set(self.__palabra_a_adivinar) == self.__adivinadas


    def actualizar(self) -> None:
        """Actualiza la interfaz gráfica a partir del estado interno."""
        self.__adivinado['text'] = self.texto_adivinado()
        self.__label_intentos['text'] = f'Te quedan {self.__intentos} intentos'
        if len(self.__erroneas) == 0:
            self.__label_erroneas['text'] = ''
        else:
            erroneas = ' '.join(self.__erroneas)
            self.__label_erroneas['text'] = f'Letras erróneas: {erroneas}'


    def probar(self, _=None) -> None:
        """
        El turno del juego, donde se comprueba la entrada del jugador y
        se actualiza el estado del juego.
        """
        c = self.__entrada.get().upper()
        self.__entrada.delete(0, tk.END)
        if len(c) == 0:
            messagebox.showerror('¡Error!', 'Entrada vacía')
            return
        if len(c) > 1:
            messagebox.showerror('¡Error!', 'La entrada sólo puede tener un carácter')
            return
        if c in self.__palabra_a_adivinar:
            self.__adivinadas.add(c)
            if self.comprobar_acierto():
                # Mostrar un mensaje diciendo que ha ganado
                messagebox.showinfo(
                    '¡Ganó!',
                    f'''¡Enhorabuena!
                    La palabra era:
                    {self.__palabra_a_adivinar}'''
                )
                self.reiniciar()
        else:
            self.__erroneas.add(c)
            self.__intentos -= 1
            if self.__intentos == 0:
                messagebox.showerror(
                    '¡Falló!',
                    f'''La palabra era:
                    {self.__palabra_a_adivinar}
                    ¡Más suerte la próxima vez!'''
                )
                self.reiniciar()
        self.actualizar()


app = Aplicacion()
app.mainloop()
