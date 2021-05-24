from dado import Dado
import pygal


#Cria um dado de 6 lados

dado = Dado()

#faz um lançamento e armazenao o resultado

resultados = []

for result_dado in range(100):
    resultado = dado.roll()
    resultados.append(resultado)
    print(resultados)


# Analisando os resultados

frequencias = []


for value in range(dado.dado_lados+1):
    frequencia = resultados.count(value)
    frequencias.append(frequencia)
    print(frequencias)

#visualizaçao dos dados

graf = pygal.Bar()
graf.tittle  =  "Resultado da jogada dos dados"
graf.x_labels = ['1','2','3','4','5','6']
graf.x_title = "Reesultado"
graf.y_tittle = "Frequencia"

graf.add('D6', frequencias)
graf.render_to_file('dados01_info.svg')


