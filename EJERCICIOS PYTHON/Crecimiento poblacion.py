#ejercicio crecimiento
def poblacion():
    n = int(input("ingrese valor n: "))
    m = int(input("ingrese valor m: "))
    dia = 1
    while m<n or m == 0:
        dia += 1
        n = n*1.02
        m = m*1.03
    print(dia)
poblacion()
    



