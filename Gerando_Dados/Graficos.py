import matplotlib.pyplot as pl

meses = [1,2,3,4,5,6,7]
valores = [1,4,8,10,12,20,30]

pl.plot(meses,valores, linewidth=4)
#Denife os titulos e define os eixos
pl.xlabel("Numero de Vendass",fontsize=24)
pl.xlabel("Valore",fontsize=14)
pl.ylabel("Meses",fontsize=14)
pl.scatter(meses,valores,c="red",edgecolors="none",s=30)
pl.show()