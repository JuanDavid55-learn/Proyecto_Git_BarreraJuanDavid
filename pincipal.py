# principal con menu y opciones
from el_json import*
from funciones_json import*
granListaPrincipal=[]
boleanito= True
while (boleanito):

    print("______________________________________________________________")
    print("                   gestión de inventario                      ")
    print("______________________________________________________________")
    print("1. ver menu de empanadas")
    print("2. hacer regirtro de una nueva empanada")
    print("3. eliminar alguna empanada del menu")
    print("4. editar el un registro de empanada")
    print("5. cerrar")
    print("--------------------------------------------------------------")
    opcion=int(input("que desea hacer? - "))
    if (opcion==1):
        from función_agregar import *
    elif(opcion==2):
        from funcion_registros import *
    elif(opcion==3):
        from funcion_eliminar import *
    elif(opcion==4):
        from funcion_editar import *
    elif (opcion):
        print("opcion no valida, vuelva a intentar")

    else:
        print("hata la proxima!!")
        boleanito= False

#### desarrollado por juan david barrera torres - T.I. 1.097.101.967