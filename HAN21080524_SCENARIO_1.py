#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:14:28 2022

@author: apple
"""
Destination = []
Num_of_destination=int(input("Please enter the number of destination"))
for i in range(Num_of_destination):
    Location_destination=input("Please enter the location of each destination:")
    Destination.append(Location_destination)
Destination_dictionary={}
n = int(input("Enter number of goods : "))
for x in Destination:
    Destination_dictionary[str(x)]=[]
for i in range(0, n):
    a=str(input("Enter the location destination:"))
    b=input("Enter the weight of good")
    if a==Destination[0]:
       Destination_dictionary[str(Destination[0])].append(b)
    if a==Destination[1]:
       Destination_dictionary[str(Destination[1])].append(b)
    if Num_of_destination>2 and a==Destination[2]:       
       Destination_dictionary[str(Destination[2])].append(b)
    if Num_of_destination>3 and a==Destination[3]:
       Destination_dictionary[str(Destination[3])].append(b)
    if Num_of_destination>4 and a==Destination[4]:
       a==Destination[4]
       Destination_dictionary[str(Destination[4])].append(b)
    if Num_of_destination>5 and a==Destination[5]:
       a==Destination[5]
       Destination_dictionary[str(Destination[5])].append(b)
    if Num_of_destination>6 and a==Destination[6]:
       a==Destination[6]
       Destination_dictionary[str(Destination[6])].append(b)
    if Num_of_destination>7 and a==Destination[7]:
       a==Destination[7]
       Destination_dictionary[str(Destination[7])].append(b)
    if Num_of_destination>8 and a==Destination[8]:
       a==Destination[8]
       Destination_dictionary[str(Destination[8])].append(b)
    if Num_of_destination>9 and a==Destination[9]:
       a==Destination[9]
       Destination_dictionary[str(Destination[9])].append(b)   
Door2 = dict(list(Destination_dictionary.items())[len(Destination_dictionary)//2:])
Door1 = dict(list(Destination_dictionary.items())[:len(Destination_dictionary)//2])
print("Door1 is:",Door1)
print("Door2 is:",Door2)       
  