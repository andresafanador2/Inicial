#terreno
def terreno():
    x = int(input("ingrese el valor del largo del terreno en metros: \n"))
    y = int(input("ingrese el valor del ancho del terreno en metros: \n"))
    a = int(input("ingrese el costo del metro de madera: \n"))
    b = int(input("ingrese el costo del metro de alambre: \n"))


def perimetro(x,y):
    per = x*2+y*2
    return per
    
def calculo(a,b,per):
    A = a * per
    B = b * per

    if A < B:
        print("sale mejor la madera")
    elif A == B:
        print("cualquiera es viable")
    elif A > B:
        print("sale mejor el alambre")
    return (A,B)
terreno()