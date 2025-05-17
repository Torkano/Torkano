#Nos piden hacer una ecuación de sumatoria hasta el valor n.

#comenzamos indicando el valor de N para su límite.

n = int(input("Ingrese el límite de la sumatoria: "))

#esto es para hacer una sumatoria teniendo como dato inicial 0.
sumatoria = 0

for i in range(1,n+1):
    suma = sumatoria + (1/i)
    sumatoria = suma

print(f"La suma total es de {sumatoria:.2f}") #este format lo vimos en la clase de calculo de promedios.
  