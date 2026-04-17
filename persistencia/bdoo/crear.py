import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree # type: ignore
from modelo import Empleado, Departamento


# Creación de las instancias:

d1 = Departamento(1, 'Informática')
d1.agregar_empleado(Empleado('111A', 'Juan Pérez', 30000.00))
d1.agregar_empleado(Empleado('222B', 'María López', 35000.00))
d2 = Departamento(2, 'Inglés')
d2.agregar_empleado(Empleado('333C', 'José Martínez', 15000.00))

# Configuración de la base de datos:

almacen = ZODB.FileStorage.FileStorage('departamentos.fs')
bd = ZODB.DB(almacen)
conexion = bd.open()
raiz = conexion.root()

raiz['departamentos'] = BTree()
raiz['departamentos'][d1.numero] = d1
raiz['departamentos'][d2.numero] = d2

transaction.commit()
conexion.close()
bd.close()
