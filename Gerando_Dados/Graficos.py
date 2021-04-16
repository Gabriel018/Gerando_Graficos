import matplotlib.pyplot as pl

meses = ["Janeiro","Fevereiro","Março","Abril"]
valores = list(range(1,5))

pl.plot(valores,meses, linewidth=4)
#Denife os titulos e define os eixos
pl.xlabel("Numero de Vendas",fontsize=24)
pl.xlabel("Valores",fontsize=14)
pl.ylabel("Meses",fontsize=14)
#pl.scatter(meses,valores,c="red",edgecolors="none",s=30)
#pl.axis([0,10,0,20])
pl.show()