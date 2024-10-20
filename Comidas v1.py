#################### Recetas (inicio) ####################

#Arroces
arroz_horno = [{'ingrediente': 'arroz', 'cantidad': "200g"}, {'ingrediente': 'preparado para arroz al horno', 'cantidad': 1}, {'ingrediente': 'tomate', 'cantidad': 1}, {'ingrediente': 'cabeza ajo', 'cantidad': 1}, {'ingrediente': 'patata', 'cantidad': 1}]
arroz_cubana = [{'ingrediente': 'arroz', 'cantidad': "200g"}, {'ingrediente': 'huevo', 'cantidad': 3}, {'ingrediente': 'bananas', 'cantidad': 3}, {'ingrediente': 'bote tomate natural', 'cantidad': "800g"}, {'ingrediente': 'caramelo', 'cantidad': 1}, {'ingrediente': 'salsa soja', 'cantidad': 1},]
arroz_anacardos = [{'ingrediente': 'botes arroz basmati', 'cantidad': 2}, {'ingrediente': 'anacardos fritos', 'cantidad': 1}, {'ingrediente': 'pechuga pollo', 'cantidad': 4}, {'ingrediente': 'aceite sésamo', 'cantidad': 1}, {'ingrediente': 'salsa soja', 'cantidad': 1}, {'ingrediente': 'dientes ajo', 'cantidad': 2},]
arroz_curry = [{'ingrediente': 'botes arroz basmati', 'cantidad': 2}, {'ingrediente': 'curry', 'cantidad': 1}, {'ingrediente': 'pimientos tricolor', 'cantidad': 1}, {'ingrediente': 'cebolla dulce', 'cantidad': 1},]

#Pescado
dorada = [{'ingrediente': 'dorada', 'cantidad': "2 lomos"}, {'ingrediente': 'ajoaceite', 'cantidad': 2}]
lubina = [{'ingrediente': 'lubina', 'cantidad': "2 lomos",}, {'ingrediente': 'ajoaceite', 'cantidad': 2}]
salmon = [{'ingrediente': 'salmón', 'cantidad': "2 lomos",}, {'ingrediente': 'mayonesa', 'cantidad': 1}, {'ingrediente': 'mostaza', 'cantidad': 1},]

#Carnes
cuartos_traseros = [{'ingrediente': 'cuartos traseros pollo', 'cantidad': 2}, {'ingrediente': 'tomate', 'cantidad': 2}, {'ingrediente': 'cebolla', 'cantidad': 1}, {'ingrediente': 'dientes ajo', 'cantidad': 2},]

#Tortillas / Revueltos
tortilla_york = [{'ingrediente': 'huevo', 'cantidad': 5}, {'ingrediente': 'jamón york', 'cantidad': 3}, {'ingrediente': 'queso havarti', 'cantidad': 3}]
tortilla_atun = [{'ingrediente': 'huevo', 'cantidad': 5}, {'ingrediente': 'bote de atún', 'cantidad': 2}, {'ingrediente': 'queso havarti', 'cantidad': 3}]
revuelto_espinacas_tomate = [{'ingrediente': 'huevo', 'cantidad': 5}, {'ingrediente': 'tomate seco', 'cantidad': 4}, {'ingrediente': 'espinacas', 'cantidad': 1}, {'ingrediente': 'queso cabra', 'cantidad': 1}, {'ingrediente': 'albahaca', 'cantidad': 1},]

#Verduras
ensalada_amor = []
ensalada_pollo_queso = []
cogollitos = []
bolitas_brocoli = []

#Varios
potaje_charo = []
hamburguesa_javier = []
calabacin_carne = []
sandwich = []
hot_dogs = []
noche_mexicana = []
espinacas_bechamel = []

pasta = [{'ingrediente': 'pasta', 'cantidad': 1}, {'ingrediente': 'salsa pasta', 'cantidad': 1}]

#################### Recetas (fin) ####################

#Menu

menusemanal = arroz_horno + arroz_anacardos + revuelto_espinacas_tomate

menusemanal_suma = {}

for i in menusemanal:
    if menusemanal_suma.get(i['ingrediente']) != None:
        menusemanal_suma[i['ingrediente']] += i['cantidad']
    else:
        menusemanal_suma[i['ingrediente']] = i['cantidad']

lst = list()
for key, val in menusemanal_suma.items():
    newtup = (val, key)
    lst.append(newtup)

for val, key in lst:
    print(val, key.title())