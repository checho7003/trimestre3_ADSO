""" Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras,
luego tres primeras y así sucesivamente hasta llegar a la última"""

def hola (cod):
    vl = len(cod)
    suma = 0
    for i in range(vl - 1):
        sub = cod[:2 + suma]
        suma += 1
        print(sub)

hola ('subrealistas')