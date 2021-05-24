import pygal

Sabores = pygal.Bar()
Sabores.tittle=("Sabores mais vendidos")
Sabores.add("Mussarela",[2,4,8,6,12,16,15,30,20,12])
Sabores.add("Calabresa",[4,3,6,7,3,4,5,6,23,4,5,6])
Sabores.add("Quatro_queijos",[2,4,8,6,12,16,15,30])
Sabores.add("MArgarita",[4,3,6,7,3,4,5,6,23,4,5,8])
Sabores.render_to_file('teste_pygal.svg')