from math import ceil,floor
def carrito():
    n_producto = int(input())
    titulo()
    valor = (cuenta(n_producto))
    descuento = calcular_descuento(valor)
    print("Total $"+str(ceil((valor - descuento))))
    print("En esta compra tu descuento fue $"+str(descuento))
    print("Gracias por tu compra")

def cuenta(n_producto):    
    suma_total = 0
    for _ in range(0,n_producto,1):
        producto = input()
        precio = int(input())
        suma_total += precio
        print(f"{producto} ${precio}")
    return suma_total  

def calcular_descuento(val_des):
    if val_des > 700000:
        d = floor(val_des*0.2)
    elif val_des > 300000:
        d = floor(val_des*0.15)
    elif val_des > 150000:
        d = floor(val_des*0.1)
    else:
        d = 0
    return d
           
def titulo():
    print("Centro Comercial Unaleño \nCompra más y Gasta Menos \nNIT: 899.999.063")
    
def parte_final(valor_ceil,precio_descuento):
    print(f"en esta compra su descuento fue ${ceil(precio_descuento)}")
carrito()