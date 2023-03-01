'''Pida una cadena por teclado y diga cual es su valor al sumar sus codigos. Cual es el 
   valor numerico de acuerdo a los códigos del alfabeto '''
v=input("pedila wacha: ")
vl=0
def u(f,vl):
    for i in f:   
        vl+=ord(i)
        print(ord(i))
    print(vl)
u(v,vl)


