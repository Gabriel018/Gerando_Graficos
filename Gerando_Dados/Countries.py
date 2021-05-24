from pygal.maps.world import COUNTRIES

#  pygal.i18n entrou em desuso
for code_country in sorted(COUNTRIES.keys()):
    print(code_country,COUNTRIES[code_country])

