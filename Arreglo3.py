#Sumar los elementos de un arreglo
arreglo = []
cant = int(input("DIme cuantos num?"))
contador = 0
while(contador < cant):
    num = int(input("Dime un num: "))
    arreglo.append(num)
    contador += 1

suma = 0
for num in arreglo:
    suma +=num

print("La suma es: ", suma)