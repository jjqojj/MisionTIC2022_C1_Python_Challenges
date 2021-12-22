# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:01:49 2021

@author: jjqoj
"""

import json

from pprint import pprint

json_ingreso=input("Ingrese la información JSON: ")
data=json.loads(json_ingreso)

componentes_falta=input("Escriba el código de los componentes faltantes: ")
com_falta_vector=componentes_falta.split(" ")

#pprint(data)
#print(componentes_falta)
#print(com_falta_vector)

valor=0
carro_compras=[]

for componentes in com_falta_vector:
    if componentes in data:
        valor+=data[componentes]
        carro_compras.append(componentes)

print(valor)

if len(carro_compras)!=0:
    for comprado in carro_compras:
        print(comprado, end=" ")


