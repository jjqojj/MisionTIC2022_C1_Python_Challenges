# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:07:57 2021

@author: jjqoj
"""

vacunas=input("Escriba la serie de vacunas aplicadas: ")
vacunas_2=vacunas.replace(" ", "") #sin espacios en blanco
vacunas_3=vacunas_2.upper() #todo Mayúscula



orden_vacunas=[]
con_vacunas=[]
if len(vacunas_3)==1:
    print(i)
    print(1)
else:
    contador=1
    for i in range(len(vacunas_3)):
        if i!=(len(vacunas_3)-1):
            if vacunas_3[i]==vacunas_3[i+1]:
                contador+=1
            else:
                orden_vacunas.append(vacunas_3[i])
                con_vacunas.append(contador)
                contador=1
    else:
        orden_vacunas.append(vacunas_3[i])
        con_vacunas.append(contador)
#print(orden_vacunas)
#print(con_vacunas)


for i in orden_vacunas:
    print(i,end=" ")


print()

for i in con_vacunas:
    print(i,end=" ")
            




    