def min_maquina():
    x0 = 1.0
    xi = x0/2.0
    while xi > 0.0:
        x0 = xi
        xi = x0/2.0
    return x0
print("el minimo numero positivo es:", end = " ")
print("en esta maquina es ", min_maquina())
min_maquina()

