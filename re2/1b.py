"""
Programar en Python un modelo orientado a objetos que simule el funcionamiento de un sistema de
turnos para atención al público.
El modelo debe contar con las siguientes clases:
La clase Ticket representa un ticket de turno. Cada ticket contiene un número y un indicador de
«atendido sí o no» (un valor lógico).
La clase Cola representa la cola de espera de los tickets. Cada cola contiene una lista de tickets y
un contador interno. Además, las colas deben responder, entre otros, a los siguientes métodos:
◦ nuevo_ticket(): crea un nuevo ticket con número incremental consecutivo, lo añade a la
cola y devuelve el ticket.
◦ siguiente(): devuelve el primer ticket no atendido y lo marca como atendido. Si no hay,
devuelve None.
◦ pendientes(): devuelve la cantidad de tickets no atendidos.
"""

class Ticket:
    def __init__(self, numero: int) -> None:
        self.__numero = numero
        self.__atendido = False

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def atendido(self) -> bool:
        return self.__atendido

    def atender(self) -> None:
        """Marca el ticket como atendido."""
        self.__atendido = True


class Cola:
    def __init__(self) -> None:
        self.__tickets: list[Ticket] = []
        self.__contador: int = 0

    def nuevo_ticket(self) -> Ticket:
        """
        Crea un nuevo ticket con número incremental consecutivo, lo añade a la
        cola y devuelve el ticket.
        """
        self.__contador += 1
        t = Ticket(self.__contador)
        self.__tickets.append(t)
        return t

    def siguiente(self) -> Ticket | None:
        """
        Devuelve el primer ticket no atendido y lo marca como atendido.
        Si no hay, devuelve None.
        """
        for t in self.__tickets:
            if not t.atendido:
                t.atender()
                return t
        return None

    def pendientes(self) -> int:
        """Devuelve la cantidad de tickets no atendidos."""
        for i, t in enumerate(self.__tickets):
            if not t.atendido:
                return len(self.__tickets) - i
        return 0


if __name__ == '__main__':
    c = Cola()
    t1 = c.nuevo_ticket()
    t2 = c.nuevo_ticket()
    assert c.pendientes() == 2
    assert c.siguiente() == t1
    assert c.pendientes() == 1
