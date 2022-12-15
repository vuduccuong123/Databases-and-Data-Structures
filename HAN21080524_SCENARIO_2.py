#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:28:56 2022

@author: apple
"""

from sys import maxsize
from itertools import permutations
List_of_distace_for_each_city=[]
List_of_city=[]
vertex=[]
Number_of_city=int(input("Plase enter the number of Destination"))
for i in range (Number_of_city):
    List_of_distace_for_each_city.append([])
    if i !=0:
        vertex.append(i)
for y in range (Number_of_city):
    Name_of_city=input("Plase enter the name of city:") 
    List_of_city.append(Name_of_city)
for a in range (Number_of_city):
    Citya=int(input("Plase enter the distance from city A to %s:" %a))
    Cityb=int(input("Plase enter the distance from city B to %s:" %a))
    List_of_distace_for_each_city[0].append(Citya)
    List_of_distace_for_each_city[1].append(Cityb)
    if Number_of_city>2:
        Cityc=int(input("Plase enter the distance from city C to %s:" %a))
        List_of_distace_for_each_city[2].append(Cityc)
    if Number_of_city>3:
        Cityd=int(input("Plase enter the distance from city D to %s:" %a))
        List_of_distace_for_each_city[3].append(Cityd)
    if Number_of_city>4:
         Citye=int(input("Plase enter the distance from city E to %s:" %a))
         List_of_distace_for_each_city[4].append(Citye)   
    if Number_of_city>5:
        Cityf=int(input("Plase enter the distance from city F to %s:" %a))
        List_of_distace_for_each_city[5].append(Cityf)     
    if Number_of_city>6:
        Cityg=int(input("Plase enter the distance from city G to %s:" %a))
        List_of_distace_for_each_city[6].append(Cityg)
    if Number_of_city>7:
        Cityh=int(input("Plase enter the distance from city H to %s:" %a))
        List_of_distace_for_each_city[7].append(Cityh)
    if Number_of_city>8:
        Cityi=int(input("Plase enter the distance from city I to %s:" %a))
        List_of_distace_for_each_city[8].append(Cityi)
    if Number_of_city>9:
        Cityk=int(input("Plase enter the distance from city K to %s:" %a))
        List_of_distace_for_each_city[9].append(Cityk)
    if Number_of_city>10:
        Cityl=int(input("Plase enter the distance from city L to %s:" %a))
        List_of_distace_for_each_city[10].append(Cityl) 
s=0
current_pathweight_list = [List_of_city[0]] 
min_path = maxsize
next_permutation=permutations(vertex)
for i in next_permutation:
		current_pathweight = 0
		k = s
		for j in i:
			current_pathweight += List_of_distace_for_each_city[k][j]
			current_pathweight_list.append(List_of_city[j])
			k = j

		current_pathweight += List_of_distace_for_each_city[k][s]
		
		if min_path > current_pathweight:
			min_path_list = current_pathweight_list
			current_pathweight_list = [List_of_city[0]]

		min_path = min(min_path, current_pathweight)
print("The shortest distance is:",min_path)
print("The optimum route is",current_pathweight_list)
 








