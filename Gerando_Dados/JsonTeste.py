import json

arquivo =  'testJson.json'
with open(arquivo) as ts:
    test_carrega = json.load(ts)


#Exibe a lista
for test_json in test_carrega:
     Nome = test_json['Nome']
     Ocupacao = test_json['Ocupcao']
     print(Nome + " " + Ocupacao)