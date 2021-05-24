import csv
from matplotlib import pyplot as plt
from datetime import  datetime


arquivo = 'sitka_weather_2014.csv'

with open(arquivo) as f1:
    reader = csv.reader(f1)
    reader_low = next(reader)
    print(reader_low)

#Exibe o cabeçalho e  suas posiçoes#
#for index,collum_reader in  enumerate(reader_low):
 #   print(index,collum_reader)

    #listas
    datas,maximas,minimas = [],[],[]

    for row in reader:
        data_event =  datetime.strptime(row[0],"%Y-%m-%d")
        datas.append(data_event)
        maxima = int(row[1])
        maximas.append(maxima)
        print(maximas)
        minima = int(row[3])
        minimas.append(minima)
        print(minimas)

    #plota o grafico
    fig = plt.figure()
    plt.plot(datas,maximas,c='red')
    plt.plot(datas,minimas,c='blue')
    #formata o grafico
    plt.title("Temperatura em (F) ano 2014")
    plt.xlabel('')
    plt.text(0,0,"Temperatura maxima",c="red")
    fig.autofmt_xdate()

plt.show()