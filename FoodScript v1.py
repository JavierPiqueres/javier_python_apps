#Version 1.0
############################################# Constantes (inicio) #############################################
#Ingrediente1
valorIngrediente1 = float(input('Introduce el porcentaje de Ingrediente1: '))
Ingrediente1 = [{'ingrediente': 'subIngrediente1', 'porcentaje': 44 / 100 * valorIngrediente1},
           {'ingrediente': 'subIngrediente2', 'porcentaje': 42 / 100 * valorIngrediente1},]

#Ingrediente2
valorIngrediente2 = float(input('Introduce el porcentaje de Ingrediente2: '))
Ingrediente2 = [{'ingrediente': 'subIngrediente3', 'porcentaje': 70.27 / 100 * valorIngrediente2},
                      {'ingrediente': 'subIngrediente4', 'porcentaje': 29.73 / 100 * valorIngrediente2},]

#Ingrediente3
valorIngrediente3 = float(input('Introduce el porcentaje de Ingrediente3: '))
Ingrediente3 = [{'ingrediente': 'subIngrediente5', 'porcentaje': 80 / 100 * valorIngrediente3},
                   {'ingrediente': 'subIngrediente6', 'porcentaje': 20 / 100 * valorIngrediente3},]


############################################# Constantes (fin) #############################################

archivo_origen = r'C:/Users/kashg/Desktop/listadeingredientes.csv'

#Modficar el archivo csv: ',' por '.' y ';' por ','   
contenido = open(archivo_origen, 'r').read()
contenido = contenido.replace(',', '.')

with open(archivo_origen, 'w') as archivo:
    archivo.write(contenido)
    archivo.close()

contenido = open(archivo_origen, 'r').read()
contenido = contenido.replace(';', ',')

with open(archivo_origen, 'w') as archivo:
    archivo.write(contenido)
    archivo.close()

#Modficar todas las palabras a minúsculas
contenido = open(archivo_origen, 'r').read()
contenido = contenido.lower()

with open(archivo_origen, 'w') as archivo:
    archivo.write(contenido)
    archivo.close()

#Importa los ingredientes mediante un archivo csv (separado por comas)
import csv
with open(archivo_origen, 'r') as f:
    csv_reader = csv.DictReader(f)
    ingr = list(csv_reader)

#Convierte los números de cadenas a números flotantes
for dicts in ingr:
    for keys in dicts:
        try:
            dicts[keys] = float(dicts[keys])
        except ValueError:
            continue
        print(ingr)

#Suma de los ingredientes importados más las constantes
ingr = ingr + Ingrediente1 + Ingrediente2 + Ingrediente3

#Receta entera, unimos duplicados
ingr_suma = {} #Diccionario vacío donde guardaremos las sumas

for i in ingr:
    if ingr_suma.get(i['ingrediente']) != None:
        #Si el valor existe, es decir, que nos devuelve diferente a None, le sumamos a la clave el valor
        ingr_suma[i['ingrediente']] += i['porcentaje']
    else:
        #Si el valor no existe, es decir, que nos devuelve a None, le asignamos una nueva clave con un valor
        ingr_suma[i['ingrediente']] = i['porcentaje']

#Resumen datos introducidos:
print('Resumen de datos introducidos:'),
print('Porcentaje de Ingrediente1:', Ingrediente1)
print('Porcentaje de Ingrediente2:', Ingrediente2)
print('Porcentaje de Ingrediente3:', Ingrediente3)

#Exportando a Excel la lista ordenada
import pandas as pd

lst = list()
for key, val in ingr_suma.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst:
    print(key, val)

df_rsss = pd.DataFrame(lst, columns = ['Porcentaje', 'Ingrediente'])
df_rsss.to_excel('C:/Users/kashg/Desktop/listadeingredientesfinal.xlsx') #Selecciona la ubicación destino del archivo y el nombre del archivo
print('Operación finalizada')