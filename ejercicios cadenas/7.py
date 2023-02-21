"""De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos 
caracteres especiales."""

def a(cad):
    vocales = 0
    consonantes = 0
    vocalesTilde = 0
    caracteres = 0
    
    cad = cad.lower()
    
    for i in cad:
        if i.isalpha():
            if i in "aeiou":
                vocales += 1
            elif i in "áéíóú":
                vocalesTilde += 1
            else:
                consonantes += 1
          
        if i not in "abcdefghijklmnñopqrstuvwxyzáéíóú":
            caracteres += 1

    print(vocales,consonantes,vocalesTilde,caracteres)

a('agúa!!_')