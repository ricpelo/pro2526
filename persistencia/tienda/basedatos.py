import ZODB
import ZODB.FileStorage
import transaction

class BaseDatos:
    def __init__(self):
        self.__almacen = ZODB.FileStorage.FileStorage('tiendaonline.fs')
        self.__bd = ZODB.DB(self.__almacen)
        self.__conexion = self.__bd.open()
        self.__raiz = self.__conexion.root()

    @property
    def raiz(self):
        return self.__raiz

    def confirmar(self):
        transaction.commit()

    def cerrar(self):
        self.__conexion.close()
        self.__bd.close()
