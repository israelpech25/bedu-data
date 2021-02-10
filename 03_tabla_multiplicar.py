#Script que calcula la tabla de multiplicar de un número

#Solicitar numero al usuario por consola
numero = int(input('¿Que numero quieres multiplicar?:'))
#El dato ingresado por el usuario es una cadena "<str>"
#Se debe convertir a numero "<int>" para poder multiplicar

for n in range(10):
    r = numero * (n+1)
    print(r)

#A continuación se muestra la tabla de multiplicar del número <nunero>
