from funciones_json import* 

nombreTem =input("cual es el nombre de la empanada que desea editar? - ") 
descripcionTem= input("nueva descripcion - ")
presioTem=input("cual es el  nuevo valor? - ") 
losNuevosIngredientes=[]
losingredientesTem=int(input("cuantos ingredientes son? - "))
for i in range(losingredientesTem):
    losingredientesTem=str()
    losNuevosIngredientes.append(losingredientesTem)
    losingredientesTem()
cantidadtTem= int(input("que catidad hay? - "))

losNuevosIngredientes.append(losingredientesTem)
granListaPrincipal=datos
for i in range(len(granListaPrincipal)):
    if (nombreTem==granListaPrincipal[i]["nombre"]):
        editar={"descripcion":descripcionTem,"precio":presioTem,"ingredientes":losNuevosIngredientes,"cantidad":cantidadtTem}
        datosAgregar(editar)