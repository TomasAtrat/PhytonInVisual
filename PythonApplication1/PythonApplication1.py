def miFuncion():
    contador = 0
    for i in list(range(10)):
        contador+= 1
    return contador

print(miFuncion())

#matriz = [1, 2, 3, 4, [5, 6, 7]]
#nombre = int(input("Escriba un número"))
#matriz.append(nombre)

#def printMatriz(matriz):
#    for x in matriz.count:
#        pass

def funcWhile():
    iterador=0
    while iterador<20:
        print(f"El iterador vale {iterador}")
        iterador+=1

def NumerosIguales(x, y):
    if(x>y):
        return x
    elif(y>x):
        return y
    else:
        return "Son iguales"

result= NumerosIguales(20, 20)

print(result)

def repetirPalabraR(iterador, palabra, cantidadVeces):
    if(iterador<cantidadVeces):
        print(palabra)
        repetirPalabraR(iterador+1, palabra, cantidadVeces)

repetirPalabraR(0, "Tomás Atrat", 10)
