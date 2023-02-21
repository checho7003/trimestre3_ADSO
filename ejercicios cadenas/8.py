"""Invente un cifrado de texto tipo murcielago o César. 
Puede utilizar alguna formula matemática para este fin."""

az = 'abcdefghijklmnñopqrstuvwxyz'

text = 'hola me llamo roman'

def a(u):

    u = u.lower()

    letraCifrada = ''

    for i in u:
        if i in az:
            posicion = az.find(i) # el método find encuentra el índice de cada letra
            posicion += 1
            if posicion >= 26:
                posicion -= 27
            letraCifrada += az[posicion]
        else:
            letraCifrada += i

    print('Texto cifrado --> ',letraCifrada)

a(text) 