# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:07:32 2021

@author: jjqojj
"""

one=str("uno")
two=str("dos")
three=str("tres")
four=str("cuatro")

affinity_score:int=1
activity_score:int=1
total_post=int(input("Ingrese el número total de post publicados en los últimos 7 días "))
print(" ")

# eq1  activity_score-4=2*total_post







# eq 2 activity_score+total_post=5*affinity_score


if total_post>=0:
    activity_score=int(2*total_post+4)
    affinity_score=int((activity_score+total_post)/5)

    print(total_post,activity_score,affinity_score)



    if affinity_score >= 0 and affinity_score <=20:
        print(one) 
    
    if affinity_score >= 21 and affinity_score <=30:
        print(two) 

    if affinity_score >= 31 and affinity_score <=50:
        print(three)

    if affinity_score > 50:
        print(four)
    


