import ZODB
import ZODB.FileStorage
from modelo import Empleado, Departamento

almacen = ZODB.FileStorage.FileStorage('departamentos.fs')
bd = ZODB.DB(almacen)
conexion = bd.open()
raiz = conexion.root()

for numero, departamento in raiz['departamentos'].items():
    print(f'El departamento número {numero} es', departamento)
    print('Y sus empleados son:')
    for empleado in departamento.get_empleados():
        print(f'- {empleado!r}')

conexion.close()
bd.close()
