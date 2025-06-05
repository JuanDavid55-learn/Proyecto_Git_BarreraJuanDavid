from funciones_json import*

granListaPrincipal=datos
eliminarEmpanada = str(input("cual empanada desea elinminar? - "))
for i in range(len(granListaPrincipal)):
    if (granListaPrincipal[i]["nombre"]==eliminarEmpanada):
        tomarDecicion = int(input("esta seguro de eliminar esta empanada?. (1.Si,2.No): "))
        if (tomarDecicion==1):
            eliminado=[]
            eliminado= granListaPrincipal.pop(granListaPrincipal[i])
            eliminado=[]
            
            datos(granListaPrincipal)
            print("ya ha sido eliminada")
        else:
            print("okey")