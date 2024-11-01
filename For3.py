#Tabla de multiplicar con ingreso por teclado.

n=int(input("Ingrese el número del que quiere saber la tabla: "))

for i in range(1,13):
    print(i, "X", n, "=", (i*n))