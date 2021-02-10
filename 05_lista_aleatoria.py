# Generar una lista con valores aleatorios

import random
from random import randint

#lista vacia que contendra
lista_aleatoria = []

elementos = int(input('Cuantos elementos necesitas?: '))

contador = 1

while contador <= elementos:
    #Generamos un valor aleatorio
    matriz = randint(1,100)

    #numero aleatorio lo multiplicamos por el numero dado por el usuario
    valor = matriz * elementos
    
    #Guardar valor aleatorio en la lista
    lista_aleatoria.append(valor)
    ###print(valor)
    ###print('Contador es menor')
    #sumar valor a contador para la siguiente vuelta
    contador = contador + 1

print(lista_aleatoria)
