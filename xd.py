#Arreglo
'''
.append(v)      Agrega al finalun elemento
.insert(i,v)    Inserta en una posicion especifica
.extend(a)      Agrega un arreglo al final de otro
a + a2          Podemos concatenar arreglos
v in array      Busca un elemento dentro del arreglo
.index(v)       Devuelve elindice del valor
.count(v)       Devueve la cantidad de veces que se tiene ese valor en el arreglo    
.remove(v)      Elimina un valor del arreglo
.clear()        Vacia el arreglo
.sort()         Ordena el arreglo ascendentemente
.reverse()      Voltea el orden del arreglo
.sort(reverse=true)      
.[2:5]          Devuelve del segundo elemento hasta el quinto
.len()          Devuelve el tamaño
.[-x]           Devuleve el valor del ultimo -x posiciones

a|b             Union
a&b             Intersección
a-b             Resta de conjuntos
a^b             Diferencia Símetrica

_               Variable fictisia
'''
import cv2

img = cv2.imread('./monedascontorno/contorno.jpg')
grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)
contornos, jerarquias = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contornos, -1, (0,255,0), 1)

cv2.imshow('img',grises)
cv2.imshow('img2',img)
cv2.imshow("umbral",umbral)
print(type(jerarquias))
cv2.waitKey(0)