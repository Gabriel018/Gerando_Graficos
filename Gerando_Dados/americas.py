import pygal

#versao obsoleta
word_m = pygal.maps.world.World()
word_m_title = "America do Norte,America Ccecntral,America do Sul"
word_m.add('America do norte',['ca','us'])
word_m.add("America central",['cr','cu','pr','pa'])
word_m.add("America do Sul",['br','ar','ve','py','uy'])

#Renderizaa o map
word_m.render_to_file('america.svg')