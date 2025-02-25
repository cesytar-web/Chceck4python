#esta es una lista:
food = ['apple', 'orange','grapes', 'bananas']

print(food)


#esta es una tupla:
mi_tupla = (48, 90, 248, 28)

print(mi_tupla[2])


#este es un numero entero:
int = 25
print(int)


# este es un numero flotante:
float = 0.2547
print(float)


#este es un numero decimal:
from decimal import Decimal
mi_decimal = Decimal(20.52)
print(mi_decimal)


#este es un diccionario:
alumno = { 
    "nombre" : "Favio",
    "edad" : 25,
    "calificacion" : 90
}
print(alumno)


#numero flotante redondeado hacia arriba:
import math

float = 0.2547

print(math.ceil(float))


#esta es la raiz cuadrada del numero flotante:
import math

print(math.sqrt(float))


#este es el primer elemento de mi diccionario:
alumno1 = list(alumno.items())[0]
print(alumno1)


#este es un elemento al final de la lista:
food = ['apple', 'orange','grapes', 'bananas']
food.append('watermelon')
print(food)


#este es el primer elemento de mi lista:
food[0] = 'pera'
print(food)


#esta es mi lista ordenada alfabeticamente:
food.sort()
print(food)


#esta es una resignacion para agregar un elemento a la tupla:

new_element_tupla = mi_tupla + (2025,)
print(new_element_tupla)
