from pygal.maps.world import COUNTRIES
def get_country(country_name):
    #devolve o codigo do pais

   for code,name in COUNTRIES.items():
     if name == country_name:
        return code
   return None
print(get_country('Brazil'))
print(get_country("Zambia"))
print(get_country("Germany"))