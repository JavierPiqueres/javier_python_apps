import random

#################### Recetas (inicio) ####################

arroces = ["arroz_horno", "arroz_cubana", "arroz_anacardos", "arroz_curry"]
pescados = ["dorada", "lubina", "salmon"]
carnes = ["cuartos_traseros"]
tortillas = ["tortilla_york", "tortilla_atun", "revuelto_espinacas_tomate"]
verduras = ["ensalada_amor", "ensalada_pollo_queso", "cogollitos", "bolitas_brocoli"]
varios = ["potaje_charo", "hamburguesa_javier", "calabacin_carne", "sandwich", 
          "hot_dogs", "noche_mexicana", "espinacas_bechamel", "pasta", "Torta del amor"]

#################### Recetas (fin) ####################

semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado"]

comidas_total = arroces + pescados + carnes + tortillas + verduras + varios

random.shuffle(comidas_total)

for l1, l2 in zip(semana, comidas_total):
    print(l1, "-", l2.title())