import math
listaA=[]
nombre=[]
cantidad=[]
precio=[]
def suma_total(cant,pre):
    contador=0
    while(contador<len(cantidad)):
        precioa = cant[contador]*pre[contador]
        listaA.append(precioa)
        contador+=1
    return sum(listaA)
def encabezado(cedula):
    print("Centro Comercial Unaleño")
    print("Compra más y Gasta Menos")
    print("NIT: 899.999.063")
    print("Cliente: "+(cedula))
    print("Art Cant Precio")
    for _ in range(0,nombre,1) and _ in range(0,cantidad,1) and _ in range(0,precio,1):
        conversion_cantidad=[int(a) for a in cantidad]
        conversion_precio=[int(b) for b in precio]
        suma_total(conversion_cantidad,conversion_precio)
        return suma_total
def descuento(precio_descuento):
    if precio_descuento > 700000:
        math.floor(precio_descuento*0.2)
    elif precio_descuento > 300000:
        math.floor(precio_descuento*0.15)
    elif precio_descuento > 150000:
        math.floor(precio_descuento*0.1)
    else:
        math.floor(precio_descuento)
    return precio_descuento
sumatotal = descuento(suma_total)
def tirilla():
    bandera=True
    while (bandera):
        x=input()
        listax=x.split( "&" )
        if listax[0]=="1":
            nombre.append(listax[1])
            cantidad.append(listax[2])
            precio.append(listax[3])
            return True
        elif listax[0]=="2":
            encabezado(listax[1])
        elif listax[0]=="3":
            return False
tirilla()