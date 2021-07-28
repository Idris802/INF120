# -*- coding: utf-8 -*-

"""
Created on Thu Feb 18 10:20:52 2021

"""

__author__ = "Idris Omar"
__email__ = "mohammed.idris.omar@nmbu.no"


rhList = [[4.276, 7.000], [4.000, 8.000], [3.771, 9.000],
          [4.443, 3.142], [3.142, 6.284], [2.565, 9.425], [2.221, 12.566]]

# A. Lagre resultatene for O og V her
resultList = []

from math import pi

r = []
h = []

for k in rhList:
    r.append(k[0])
    h.append(k[1])
    
    
#  B. beregner O og V 
overflate_O = [(2 * pi * r ** 2) + (2 * pi * r * h) for r, h in rhList]
volum_V = [pi * r ** 2 * h for r, h in rhList]

# C. skriver ut r, h, O og V på skjermen med tre desimalers nøyaktighet
# D. lagrer r, h, O og V i en liste som heter resultList. Denne listen er også nøstet (nested) og ser slik ut når programmet er ferdig kjørt
for r, h, O, V in zip(r, h, overflate_O, volum_V):
    resultList.append([r, h, O, V])
    print('{0:.3f}, {1:.3f}, {2:.3f}, {3:.3f}'.format(r, h, O, V))
print(resultList)

"""
Deretter anslå du hvor mye større h bør være enn r
for å få best mulig utnyttelse av råmaterialene 
(størst mulig volum i forhold til overflate). 
Vi er ikke interessert i en analytisk løsning, 
kun et anslag ut fra beregningene du gjør.

Svar:
    For at vi skal få mest mulig råmaterie altså størst mulig volum i forhold 
    til overflate må h være dobbelt så stor som r.
    
"""



    
