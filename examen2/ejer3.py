"""
Programar en Python un modelo orientado a objetos del funcionamiento de un televisor.
Un televisor:
Puede estar encendido o apagado.
Tiene un nivel de volumen comprendido entre 0 y 30.
Tiene un puerto USB que le permite reproducir contenido multimedia almacenado en un pendrive o
disco duro externo. Para ello, debemos crear una clase llamada Soporte cuyas instancias representen
soportes de almacenamiento externo. El constructor de la clase recibe una lista con el contenido
multimedia, que son cadenas que contienen cada una el nombre de un archivo multimedia.
Los soportes deben responder, entre otros, a los métodos:
playlist(): devuelve una tupla con todos su contenido multimedia. Cada elemento de esa tupla
será una cadena que contiene el nombre del archivo correspondiente.
reproducir(indice): simula la reproducción del archivo almacenado en la posición indicada
por indice, devolviendo el nombre del archivo. Lanza una excepción IndexError si el archivo
correspondiente no existe.
El televisor debe responder, entre otros, a los métodos:
encender() / apagar(): enciende/apaga el televisor; devuelve el propio objeto televisor.
subir_volumen(): sube el volumen de uno en uno si el televisor está encendido (si está apagado,
no hace nada), siempre dentro de los límites permitidos; devuelve el propio objeto televisor.
bajar_volumen(): baja el volumen de uno en uno si el televisor está encendido (si está apagado,
no hace nada), siempre dentro de los límites permitidos; devuelve el propio objeto televisor.
volumen(): devuelve el nivel de volumen del televisor.
conectar(soporte): conecta el soporte al puerto USB; devuelve el propio objeto televisor.

desconectar_si_conectado(): desconecta el soporte que tuviera conectado en el puerto USB (si
no hubiera ninguno, no hace nada); devuelve el propio objeto televisor.
reproducir_si_conectado(): devuelve una tupla con los nombres de los archivos que hay en el
soporte que tiene conectado a su puerto USB; si no hubiera ninguno o el televisor estuviese
apagado, devuelve una tupla vacía.

Tests: Partiendo de:
soporte = Soporte(["Batman.mp4", "Superman.mp4"])
los tests son:
Televisor().encender().bajar_volumen().volumen() == 0
Televisor().subir_volumen().encender().subir_volumen().volumen() == 1
Televisor().conectar(soporte).reproducir_si_conectado() == ()
Televisor().conectar(soporte).encender().reproducir_si_conectado() == ("Batman.mp4", "Superman.mp4")
"""

class Soporte:
    def __init__(self, lista: list[str]) -> None:
        self.__contenido = lista[:]
        
    def playlist(self) -> tuple[str]:
        return tuple(self.__contenido)

    def reproducir(self, indice: int) -> str:
        return self.__contenido[indice]
    
class Televisor:
    def __init__(self) -> None:
        self.__encendido: bool = False
        self.__volumen: int = 0
        self.__soporte: Soporte | None = None
        
    def encender(self) -> 'Televisor':
        self.__encendido = True
        return self
        
    def apagar(self) -> 'Televisor':
        self.__encendido = False
        return self
        
    def volumen(self) -> int:
        return self.__volumen

    def subir_volumen(self) -> 'Televisor':
        if self.__encendido and self.volumen() < 30:
            self.__volumen += 1
        return self
    
    def bajar_volumen(self) -> 'Televisor':
        if self.__encendido and self.volumen() > 0:
            self.__volumen -= 1
        return self
    
    def conectar(self, soporte: Soporte) -> 'Televisor':
        self.__soporte = soporte
        return self
    
    def desconectar_si_conectado(self) -> 'Televisor':
        self.__soporte = None
        return self
    
    def reproducir_si_conectado(self) -> tuple[str]:
        if not self.__encendido or self.__soporte is None:
            return ()
        return self.__soporte.playlist()


soporte = Soporte(["Batman.mp4", "Superman.mp4"])
assert Televisor().encender().bajar_volumen().volumen() == 0
assert Televisor().subir_volumen().encender().subir_volumen().volumen() == 1
assert Televisor().conectar(soporte).reproducir_si_conectado() == ()
assert Televisor().conectar(soporte).encender().reproducir_si_conectado() == ("Batman.mp4", "Superman.mp4")