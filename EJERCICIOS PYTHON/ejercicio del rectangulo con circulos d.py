#ejercicio del rectangulo con circulos diferentes
def area_rectangulo(l,a):
    return l*a
l = float(input())
a = float(input())
l1 = float(input())
a1 = float(input())
from math import pi
def area_circulo(r):
    return pi*(r**2)
radio_circulo_1 = float(input())
radio_circulo_2 = float(input())
area_total = area_rectangulo(l,a) + area_rectangulo(l1,a1) + area_circulo(radio_circulo_1) + area_circulo(radio_circulo_2)
print("suma total = ", area_total)