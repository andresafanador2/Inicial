#productos
x = input("ingrese los nombres de los productos separados por espacios: \n")
y = (input("ingrese el precio de los productos separados por espacios: \n"))
lista_x = x.split(" ")
lista_y =y.split(" ")
a = [int(x) for x in lista_y]
suma = sum(a)
if suma < 35000:
    print("mejor los productos por separado")
elif suma == 35000:
    print("no hay diferencia entre los individuales y el combo")
elif suma > 35000:
    print("es mejor el combo")
