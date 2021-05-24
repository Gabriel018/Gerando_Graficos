import json
import pygal
from codigo_paises import  get_country
from pygal.style import LightColorizedStyle,RotateStyle
#carrega os dados em uma lista
arquivo = 'population_data.json'
with open(arquivo) as ar:
    pop_data = json.load(ar)
#exibe  a populaçao de caada pais
cc_poulacion = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
       country_name = pop_dict['Country Name']
       populacao = int(float(pop_dict['Value']))
       code = get_country(country_name)
       if code:
           cc_poulacion[code] = populacao

#Agrupa paises em 3 nives

cc_pop1,cc_pop2,cc_pop3 = {},{},{}
for cc, pop in cc_poulacion.items():
  if pop < 1000000:
        cc_pop1[cc] = pop
  elif  pop < 10000000:
       cc_pop2[cc] = pop
  else: cc_pop3[cc] = pop

#ve quantos paises estao em cada nivel
print(len(cc_pop1),len(cc_pop2),len(cc_pop3))


wp_Style = LightColorizedStyle
wp = pygal.maps.world.World(style=wp_Style)
wp.title = "populaçao mundial 2010 por paises"
wp.add('0-10m',cc_pop1)
wp.add('10m-1bn',cc_pop2)
wp.add('>1b',cc_pop3)
wp.render_to_file("world_populacion.svg")