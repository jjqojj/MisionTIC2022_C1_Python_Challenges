# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 19:40:49 2021

@author: jjqoj
"""

mesas_P=str(input("Ingrese sin espacios las mesas del primer Piso ")) # Mesas primer piso
mesas_S=str(input("Ingrese sin espacios las mesas del segundo Piso ")) # Mesas segundo piso
mesas_servidas=str(input("Ingrese las mesas que fueron servidas "))

#total_mesas_P=len(mesas_P)
#total_mesas_S=len(mesas_P)

servicios_mesaP=0
servicios_mesaS=0

total_servicios=len(mesas_servidas)

for i in range(total_servicios):
    if mesas_servidas[i] in mesas_P:
        #print("Primer Piso")
        servicios_mesaP+=1
    elif mesas_servidas[i] in mesas_S:
        #print("Segundo Piso")
        servicios_mesaS+=1
    if servicios_mesaP>servicios_mesaS:
        print("P",end="")
    elif servicios_mesaP<servicios_mesaS:
        print("S",end="")
    else:
        print("I",end="")
        


    