#reto 4
import json
import requests
from pprint import pprint
from math import ceil,floor

def total_x_cobro(val_des):
    if val_des > 700000:
        d = floor(val_des*0.2)
    elif val_des > 300000:
        d = floor(val_des*0.15)
    elif val_des > 150000:
        d = floor(val_des*0.1)
    else:
        d = 0
    return d
    
def main():
    ingresar = ''
    ingresar = input(':')
    repuesta_servidor = requests.get(ingresar)
    salida = json.loads(repuesta_servidor.text)
    for cliente in salida:
        print("Centro Comercial Unaleño \nCompra más y Gasta Menos \nNIT: 899.999.063")
        print(f'Cliente: {cliente["cliente"]}\nArt Cant Precio')
        a=0
        for producto in range(len(cliente["productos"])):
            suma =cliente["productos"][producto]["precio unitario"] * cliente["productos"][producto]["cantidad"]
            print(f'{cliente["productos"][producto]["nombre"]} x{cliente["productos"][producto]["cantidad"]} ${suma}')
            a += suma
        descuento = int(total_x_cobro(a))
        total = ceil(a-descuento)
        print("Total: $"+str(total))
        print("En esta compra tu descuento fue $"+str(descuento))
        print("Gracias por tu compra \n---")
        total_x_cobro(a)
main()