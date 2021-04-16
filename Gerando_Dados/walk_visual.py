import matplotlib.pyplot as pl

from caminho_aleatorio import RandomWalk

#Cria um passeio aleatorio e gera no mapa

walk = RandomWalk()
walk.fill_walk()
pl.scatter(walk.x_valores,walk.y_valores)
pl.show()