def suma(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s
x = int(input("ingrese numero: "))
print(suma(x))
suma(x)


frutas = ["pera", "mango", "guayaba", "lulo"]
for f in frutas:
    print(f)
    if f == "guayaba":
        break

