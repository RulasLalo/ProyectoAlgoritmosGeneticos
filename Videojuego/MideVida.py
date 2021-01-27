import math
import random
from random import sample

class MideVida:
    
    def __init__(self):
        self.individuos=0
        self.rango=8
        self.lista_rango=[]
        self.aleatorio=0
        self.principal()

    def principal(self):
        for i in range(self.rango):
            self.lista_rango.append(i)
        
        print(self.lista_rango)

obj=MideVida()