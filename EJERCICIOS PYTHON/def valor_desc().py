
def valor_desc(cantidad,precio):
    if 5 >= cantidad < 10:
        precio = precio - (precio*0.05)
    elif 10 >=  cantidad <20:
          precio = precio - (precio*0.1)
    elif 20 > cantidad:
        precio = precio-(precio*0.2)
    return cantidad*precio
def main():
    producto = int(input(" Ingrese la cantidad de productos iguales: "))
    valor = int(input(" Ingrese el valor del producto: "))
    print("el valor a pagar es: ", valor_desc(producto, valor))        
main()





