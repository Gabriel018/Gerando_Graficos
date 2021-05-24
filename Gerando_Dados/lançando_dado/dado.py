from random import  randint


class Dado():

 def __init__(self, dado_lados=6):
     #classe que representa um daados
     self.dado_lados = dado_lados

 def roll(self):
     #Devolver um lado aleatorio entre 1 e 6

     return randint(1,self.dado_lados)



