Nombre = input("Producto: ")
Costounitario = int(input("CU: "))
PrecioVPublico = int(input("PVP: "))
Unidadesdisponibles = int(input("Unidades Disponibles: "))
print("Producto: " + Nombre)
print("CU: " + "$"+ str(Costounitario))
print("PVP: " + "$"+ str(PrecioVPublico))
print("Unidades Disponibles: "+ str(Unidadesdisponibles))
Ganancia = (PrecioVPublico-Costounitario)*Unidadesdisponibles
print("Ganancia: " + "$" +str(Ganancia))