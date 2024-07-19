#este programa muestra como podemos aproximar un punto a travez de una funcion. Dado n puntos formamos un polinomio de n-1 grados, que me permitira obtener la proximacion con cierto grado de error al punto buscado.

from funciones import obtener_puntos

print("Para empezar buscando nuetra aproximacion, por favor ingrese el punto al cual quiere aproximar")
valorAproximacion= int()

print("Ahora escriba por favor los distintos puntos que usaremos para crear el polinomio. Para ello escriba el valor de X, separado de una coma, y luego Y. Ejemplo: [x,y];[2,23]. Para finalizar escriba E")

x,y= obtener_puntos()

print (x,y)


