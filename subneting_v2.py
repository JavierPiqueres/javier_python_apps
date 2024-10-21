import re

def validar_datos_introducidos(pregunta):
    patron = r'\b[0-9]{1,3}+\.+[0-9]{1,3}+\.+[0-9]{1,3}+\.+[0-9]{1,3}\b'
    
    while True:
        dato = input(pregunta)
        
        if re.match(patron, dato):
            print("Dato aceptado.")
            return dato
        else:
            print(f"Dato no aceptado. Por favor, {pregunta.lower()}")

entrada = validar_datos_introducidos("Escribe la dirección IPv4: ")
partes = entrada.split(".")

ip = []
for x in partes:
    ip.append(int(x))

#

entrada = validar_datos_introducidos("Escribe la máscara de subred: ")
partes = entrada.split(".")

netmask = []
for x in partes:
    netmask.append(int(x))

#

entrada = validar_datos_introducidos("Escribe la nueva máscara de subred: ")
partes = entrada.split(".")

new_netmask = []
for x in partes:
    new_netmask.append(int(x))

#

print(f"Dirección IPv4: {ip}")
print(f"Máscara de subred: {netmask}")
print(f"Nueva máscara de subred: {new_netmask}")

#def para pasar de decimal a binario
def decimal_a_binario(numero):
    binario = bin(numero)[2:]
    binario_completo = binario.zfill(8)
    return binario_completo

#def para pasar de binario a decimal
def binario_a_decimal(numero):
    binario = numero
    resultado_decimal = int(binario, 2)
    return resultado_decimal

#def para dividir listas en sublistas de 8
def dividir_lista(lista):
    sublistas = []
    for i in range(0, len(lista), 8):
        sublista = lista[i:i + 8]
        sublistas.append(sublista)
    return sublistas

#def unir elementos de lista en 1 solo elemento unido
def unir_lista(lista_a_unir):
    cadena_unida = "".join(lista_a_unir)
    return cadena_unida

#calculos / network
def network_def(lst_to_go, ip_binario, netmask_binario):
    for bit_ip_network, bit_netmask_network in zip(ip_binario, netmask_binario):
        if bit_netmask_network == "1":
            lst_to_go.append(bit_ip_network)
        elif bit_netmask_network == "0":
            lst_to_go.append("0")

#calculos / broadcast
def broadcast_def(lst_to_go, ip_binario, netmask_binario):
    for bit_ip_network, bit_netmask_network in zip(ip_binario, netmask_binario):
        if bit_netmask_network == "1":
            lst_to_go.append(bit_ip_network)
        elif bit_netmask_network == "0":
            lst_to_go.append("1")

#Direcciones a listas en binario
def pasar_bits_a_lista(lista_vacia ,direc_origen):
    for x in direc_origen:
        for y in x:
            lista_vacia.append(y)

#def para calcular los bits de subred
def bits_subred(direccion_binario):
    counter = 0
    for item in reversed(direccion_binario):
        if item == "0":
            counter = counter + 1
        elif item == "1":
            break
    x = 32 - counter
    return x

#########

print(f"Dirección IP en decimal: {ip}")
print(f"Máscara de subred en decimal: {netmask}")
print(f"Nueva máscara de subred en decimal: {new_netmask}")

print("----")

ip_binario = []
netmask_binario = []
new_netmask_binario = []

for ip_byte in ip:
    ip_bin = decimal_a_binario(ip_byte)
    ip_binario.append(ip_bin)

for netmask_byte in netmask:
    netmask_bin = decimal_a_binario(netmask_byte)
    netmask_binario.append(netmask_bin)

for new_netmask_byte in new_netmask:
    new_netmask_bin = decimal_a_binario(new_netmask_byte)
    new_netmask_binario.append(new_netmask_bin)

print(f"Dirección IP en binario: {ip_binario}")
print(f"Máscara de subred en binario: {netmask_binario}")
print(f"Nueva máscara de subred en binario: {new_netmask_binario}")

print("----")

#Direcciones a listas en binario
lista_bits_ip = []
lista_bits_netmask = []
lista_bits_new_netmask = []
            
pasar_bits_a_lista(lista_bits_ip, ip_binario)
pasar_bits_a_lista(lista_bits_netmask, netmask_binario)
pasar_bits_a_lista(lista_bits_new_netmask, new_netmask_binario)

print(lista_bits_ip)
print(lista_bits_netmask)
print(lista_bits_new_netmask)

print("----")

#Dirección de red / network
network = []

network_def(network, ip_binario[0], new_netmask_binario[0])
network_def(network, ip_binario[1], new_netmask_binario[1])
network_def(network, ip_binario[2], new_netmask_binario[2])
network_def(network, ip_binario[3], new_netmask_binario[3])

print(f"La network en binario es: {network}")

#Dirección de broadcast
broadcast = []

broadcast_def(broadcast, ip_binario[0], new_netmask_binario[0])
broadcast_def(broadcast, ip_binario[1], new_netmask_binario[1])
broadcast_def(broadcast, ip_binario[2], new_netmask_binario[2])
broadcast_def(broadcast, ip_binario[3], new_netmask_binario[3])

print(f"La broadcast en binario es: {broadcast}")

print("----")

#Dirección de network/broadcast unidas
print("Aqui está la network en binario, unida", unir_lista(network))
network_united = unir_lista(network)

print("Aqui está la broadcast en binario, unida", unir_lista(broadcast))
broadcast_united = unir_lista(broadcast)

print("----")

#Dirección de network/broadcast separadas
print("Aquí está la network en binario, separada en bytes ", dividir_lista(network_united))
network_splited = dividir_lista(network_united)

print("Aquí está la broadcast en binario, separada en bytes ", dividir_lista(broadcast_united))
broadcast_splited = dividir_lista(broadcast_united)

print("----")

#Dirección de network/broadcast en decimal
print("Dirección de network:")
for bytes in network_splited:
    print(binario_a_decimal(bytes))

print("----")

print("Dirección de broadcast:")
for bytes in broadcast_splited:
    print(binario_a_decimal(bytes))

print("----")

######Resumen de toda la información######
print("Resumen de toda la información de la red:\n")

#Cantidad de bits de subred
cantidad_bits_subred = bits_subred(lista_bits_new_netmask) - bits_subred(lista_bits_netmask)
print(f"Cantidad de bits de subred: {cantidad_bits_subred}")

#Cantidad de subredes creadas
cantidad_subredes_creadas = 2**cantidad_bits_subred
print(f"Cantidad de subredes creadas: {cantidad_subredes_creadas}")

#Cantidad de bits de host por subred
cantidad_bits_host_subred = 32 - bits_subred(lista_bits_new_netmask)
print(f"Cantidad de bits de host por subred: {cantidad_bits_host_subred}")

#Cantidad de hosts por subred
cantidad_hosts_subred = 2**cantidad_bits_host_subred - 2
print(f"Cantidad de hosts por subred: {cantidad_hosts_subred}")

#Dirección de red de esta subred
direccion_de_network = []
for bytes in network_splited:
    direccion_de_network.append(binario_a_decimal(bytes))
print(f"Dirección de red de esta subred: {direccion_de_network}")

#Dirección IPv4 del primer host de esta subred
direccion_primer_host_subred = direccion_de_network
direccion_primer_host_subred[-1] += 1
print("Dirección IPv4 del primer host de esta subred:", direccion_primer_host_subred)

#Dirección IPv4 de difusión de esta subred
direccion_de_broadcast = []
for bytes in broadcast_splited:
    direccion_de_broadcast.append(binario_a_decimal(bytes))
print(f"Dirección IPv4 de difusión de esta subred: {direccion_de_broadcast}")

#Dirección IPv4 del último host de esta subred
direccion_ultimo_host_subred = direccion_de_broadcast
direccion_ultimo_host_subred[-1] -= 1
print("Dirección IPv4 del primer host de esta subred:", direccion_ultimo_host_subred)