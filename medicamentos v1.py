##### Listado de Medicamentos #####

medicamentos = [
{'medicamento': 'paracetamol', 'caducidad': '2/4/25'},
{'medicamento': 'enantium', 'caducidad': '2/11/22'},
{'medicamento': 'ibuprofeno', 'caducidad': '01/01/26'}
]

##### Fin Listado de Medicamentos #####

from datetime import datetime

def caducado(medicamentos):
    hoy = datetime.now()
    for med in medicamentos:
        fecha_caducidad = datetime.strptime(med['caducidad'], '%d/%m/%y')
        if fecha_caducidad < hoy:
            print(f"El medicamento '{med['medicamento']}' está caducado.")
        else:
            print(f"El medicamento '{med['medicamento']}' no está caducado.")

caducado(medicamentos)