from funciones_json import*

nombreEmpanada=str(input("nombre: "))
descripcion=str(input("descripción: "))
presio=str(input("presio: "))
ingredientes=[]
los_ingredientes=int(input("cuantos ingredientes son? - "))
for i in range(los_ingredientes):
    ingredienteN=str()
    los_ingredientes.append(ingredienteN)
    ingredienteN()
cantidadDisponible=str(input("cantidad: "))

nuevaEmpanada={
    "nombre": nombreEmpanada,
    "descripcion": descripcion,
    "precio": presio,
    "ingredientes": los_ingredientes,
    "cantidad": cantidadDisponible
    }
granListaPrincipal=datos
granListaPrincipal.append(nuevaEmpanada)
nuevaEmpanada={}

