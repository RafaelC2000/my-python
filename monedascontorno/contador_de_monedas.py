import cv2             #libreria para reconocer los contornos
import numpy

#NOTA: para evitar errores de src void, llamar desde la carpeta a nivel de la de codigo
im = cv2.imread('./monedascontorno/monedas.jpg') 
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
gblur = cv2.GaussianBlur(imgray, (5,5), 0)
bord = cv2.Canny(gblur, 100,200)
kernel = numpy.ones((3,3), numpy.uint8)
cierre = cv2.morphologyEx(bord, cv2.MORPH_CLOSE, kernel)
contornos, jerarquias = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contornos, -1, (255,0,0), 2)

cv2.imshow('Monedas', im)
cv2.imshow('Monedas Grises', imgray)
cv2.imshow('Monedas G Sin Ruido', gblur)
cv2.imshow('Monedas Bordes', bord)
cv2.imshow('Monedas Cierre', cierre)
print('monedas encontradas: {}'.format(len(contornos)))
cv2.waitKey(0)