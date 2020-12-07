#Leer 4 valores enteros A, B, C y D. Si B es mayor que C y D es mayor que A y si la suma de C y D es mayor que la suma de A y B y si C y D fueran valores positivos y si A es par, escriba el mensaje “Valores aceptados”. De lo contrario, escriba el mensaje “Valores no aceptados”.
# input 5, 6, 7, 8 output valores no aceptados// input: 2, 3, 2 ,6 output Valores aceptados

def valores_enteros():
    a = int(input("ingrese el valor de A: "))
    b = int(input("ingrese el valor de B: "))
    c = int(input("ingrese el valor de C: "))
    d = int(input("ingrese el valor de D: "))
    if b > c and d > a and c+d > a+b and c >= 0 and d >= 0 and a %2 == 0:
        print("Valores aceptados")
    else:
        print("valores no aceptados")
valores_enteros()



