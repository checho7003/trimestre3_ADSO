"""Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez"""
h=input("Ingrese un texto que desee: \n ")
h1=""
def hola(a,h):
    for i in a:
        if i not in h:
            h+=i
    return len(h)

print(hola(h,h1))