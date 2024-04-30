impares = (1,3,5,7,9,11,13,15,17,19)
print(type(impares))

print(impares[4])
print(impares[-6])
print(impares[:4])
print(impares[4:])
print(impares[4:6])
print(impares[-4:-1])


# lista con los dato
lista_afanumerica = ("a",1,"b",2,"c",3,"d")
# imprimir la lista numerica 
print(lista_afanumerica)
#len es contadore de elementos
print(len(lista_afanumerica))
#len es contadore de elementos medio dividido 2 para el centro
medio = len(lista_afanumerica)//2
#imprimir lista numerica y sacar el medio
print(lista_afanumerica[medio])

impares = [1,3,5,7,9,11,13,15,17,19] #len devuelve un resultado respuesta
tamanio = (len(impares))
print(len(impares))  # reverse no devuelve valor, reverse de atras a adelante, la funcion reverse opera sobre la variable impares
impares.reverse()
print(impares) 

matriz=[
    [1,2,3,4,5],   #fila 0
    [6,7,8,9,10],  #fila 1
    [11,12,13,14,15] #fila 2
]
print(matriz[1][2]) #imprimir(matris[fila 1][posisision2])

numero = input('5: ')
numero = int(numero)
if numero % 2 == 0:
     print (f'El numero {numero} es par')
else:
     print (f'El numero {numero} es impar')
