#Ejercicio Rectangulo
def area_rectangulo(l,a):
    """input: el largo del rectangulo
    esta dada por l.
    input: el ancho del rectangulo esta 
    dada por a.
    Return: area del rectangulo"""
    return l*a

l = float(input("por favor ingrese el largo del rectangulo: "))
a = float(input("por favor ingrese el ancho del rectangulo: "))
print("el area del rectangulo es: ", area_rectangulo(l,a))

from math import pi
def area_circulo(r):
    """
    input: r corresponde al area
    del circulo.
    return: pi*(r**2)
    """
    return pi*(r**2)
radio = float(input("por favor ingresa el valor del radio: "))
resultado = area_circulo(radio)
print("el valor del area del circulo es : ", resultado)

print("teniendo en cuenta que son dos circulos y ambos tienen los mismos tamaños, los valores son: ", resultado, "y", resultado)
area_total = area_rectangulo(l,a) + area_circulo(radio)*2
print("el area total es: ", area_total)