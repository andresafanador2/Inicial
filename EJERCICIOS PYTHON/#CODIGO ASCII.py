#CODIGO ASCII
def codigo_ascci():
    entero = int(input("ingrese un numero entero:" ))
    while(entero < 65 or entero > 90):
        entero = int(input("ingrese un numero entero:" ))
    print("su numero corresponde a: ", chr(entero))
codigo_ascci()

def main():
    entero = int(input("Ingrese un numero entero: "))
    
    #opcion 1
    while(entero<65 or entero>90):
        entero = int(input("Ingrese un numero entero:"))

    # opcion 2
    while not (65<=entero and 90 >=entero ):
        entero = int(input("Ingrese un numero entero:"))

    print("Su número corresponde a: ", chr(entero) )
main()