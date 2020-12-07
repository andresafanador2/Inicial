from math import ceil,floor
nombre_de_productos = []
Cantidad_de_productos = [] 
precio_de_productos = []
total_cobro = []
def datos(producto,cantidad,valor):
    nombre_de_productos.append(producto)
    Cantidad_de_productos.append(cantidad)
    precio_de_productos.append(valor)
    return True

def total_x_cobro(cantidad,valor):
    suma_cobro = 0
    while(suma_cobro<len(cantidad)):
        tc = cantidad[suma_cobro]*valor[suma_cobro]
        total_cobro.append(tc)
        suma_cobro += 1
    return total_cobro
        
def descuento(val_des):
    if val_des > 700000:
        d = floor(val_des*0.2)
    elif val_des > 300000:
        d = floor(val_des*0.15)
    elif val_des > 150000:
        d = floor(val_des*0.1)
    else:
        d = 0
    return d

def tirilla(usuario):
    print("Centro Comercial Unaleño \nCompra más y Gasta Menos \nNIT: 899.999.063")
    print("cliente: "+usuario)
    print("Art Cant Precio")
    a = [int(x) for x in Cantidad_de_productos]
    b = [int(x) for x in precio_de_productos]
    total_x_cobro(a,b)
    repeticion = 0
    while(repeticion<len(nombre_de_productos)): # for _ in range (len(nombre_de_productos))
        print(str(nombre_de_productos[repeticion]),"x"+str(Cantidad_de_productos[repeticion]),str(total_cobro[repeticion]))
        repeticion += 1
    c = [int(x) for x in total_cobro]

    suma = sum(c)
    descuento_compra = descuento(suma)
    int(descuento_compra)
    print("Total: $"+str(ceil(suma-descuento_compra)))
    print("En esta compra tu descuento fue $"+str(descuento_compra))
    print("Gracias por tu compra \n---")
    del nombre_de_productos[:]
    del Cantidad_de_productos[:]
    del precio_de_productos[:]
    del total_cobro[:]
    return True

def main():
    bandera = True
    while (bandera):
        insertar = input()
        datos_list = insertar.split("&")
        if datos_list[0] == "1":
            datos(datos_list[1],datos_list[2],datos_list[3])
        elif datos_list[0] == "2":
            tirilla(datos_list[1])
        elif datos_list[0] == "3":
            return False
main()