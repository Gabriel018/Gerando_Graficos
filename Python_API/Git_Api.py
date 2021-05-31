import requests
import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url =  'https://api.github.com/search/repositories?q=language:python&sort=stars'
res = requests.get(url)
#Armazena a resposta da api em um variavel
response = res.json()
print("Total de repositorios:", response['total_count'])
#processa o resultado

#explora informaçoes sobre o repositorio
response_dicts = response['items']
#Analisa o primeiro repositorio

response_dict = response_dicts[0]
names, plot_dicts = [],[]






print("Informaçoes sobre os Repositorios")
for response_dict in response_dicts:
 names.append(response_dict['name'])


 plot_dict = {
     'value':response_dict['stargazers_count'],
     'xlink': response_dict['html_url'],
 }

 plot_dicts.append(plot_dict)
 print("Name", response_dict['name'])
 print("Owner",response_dict['owner'],['login'])
 print("Stars",response_dict['stargazers_count'])
 print("Repositorio",response_dict['html_url'])
 print("Keys: ", len(response_dict))
 print("Repositorios: ", len(response_dicts))
 print("Status code: ",res.json())
 print(response.keys())
for k in sorted(response_dict.keys()):
    print(k)

#cri a visualizaçao
Stilo = LS('#498893',base_style=LCS)
char = pygal.Bar(style=Stilo,x_label_rotation=45,show_legend=False)
char.title = ("Mostra os projeto do Git")
char.x_labels = names
char.add('',plot_dicts)
char.render_to_file("pythonapi.svg")
#alisa o primeiro repositorio