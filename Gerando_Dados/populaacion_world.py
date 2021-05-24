import pygal

pop_mund = pygal.maps.world.World()
pop_mund.title = ('Poluçao dos Paises')
pop_mund.add("America do sul", {'br':4803545,'ve':548722,'py':542154})

pop_mund.render_to_file("Americaa_pop.svg")