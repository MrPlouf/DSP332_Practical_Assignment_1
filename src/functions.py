#Use this file to create the game logic and functions

import random as rd

#Creation of a simple function that generate a simple array of 5 numbers (see task for details)
def generation_numbers():
    nombres = []
    while len(nombres)<5:
        numero = rd.randint(10000,20000)
        if numero % 6 == 0:
            nombres.append(numero)
    return nombres

