﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 21 de novembro de 2018

@author: leonardotome

"""


print("Welcome to Multiplication Table generator!") #Show welcome message

print("")

num=int(input("Insert the multiplied number:  ")) #User input: multiplied number

lin=int(input("How many lines do you want?  ")) #User input: how much lines?

print("")

print("Here's the multiplication table for", num,"with",lin,"lines.") #Show title

print("")

for i in range(num, num+1): 
	for j in range(1, lin+1):
		print(i," x ",j," = ",i*j)


print("")