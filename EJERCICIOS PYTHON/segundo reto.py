from math import ceil
def tirilla_pagos():
    n_producto = int(input("ingrese # de productos: "))

def cuenta(n_producto):
    suma_total = 0
    for _ in range(0,n_producto,1):
        producto = input()
        precio = int(input())
        suma_total += 1
        print(f"{producto} ${precio}")
    return suma_total  

def descuento():
    if  