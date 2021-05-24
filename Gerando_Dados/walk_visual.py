import matplotlib.pyplot as pl

from caminho_aleatorio import RandomWalk

#Cria um passeio aleatorio e gera no mapa

while True:
 #cria uma rota aleatoria e plota
 walk = RandomWalk()
 walk.fill_walk()
 #Denife o tammanho da tela
 pl.figure(figsize=(10, 6))
 pl.scatter(walk.x_valores,walk.y_valores, s=25)
 pl.show()

 continuar = input("Deseja continuar(y/n)?")
 if continuar == 'n':
   break

