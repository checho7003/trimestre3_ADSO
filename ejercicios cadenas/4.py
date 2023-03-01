'''Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas'''
vl=input("Escriba lo que quiera: ")
def a(u):
    print(u.lower())
    print(u.upper())
    print(u.title())
    print(u.swapcase())
    print(u.capitalize())
    print(u.casefold())

a(vl)

