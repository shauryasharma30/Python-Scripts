# -*- coding: utf-8 -*-
"""


@author: shaurya
"""
#this is dobble game where I used alphabets as symbols

import string
import random
symbols=[]
symbols=list(string.ascii_letters)
card1 = [0]*7
card2 = [0]*7
pos1 = random.randint(0,6)
pos2 = random.randint(0,6)
# pos1 and pos2 are the position of the same symbol
sameSymbol = random.choice(symbols)
symbols.remove(sameSymbol)
if(pos1 == pos2):
    card1[pos1] = sameSymbol
    card2[pos2] = sameSymbol
else:
    card1[pos1] = sameSymbol
    card2[pos2] = sameSymbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while (i<7):
    if(i!=pos1 and i!=pos2):
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i=i+1
print(card1)
print(card2)

ch = input("enter the same symbol: ")
if (ch == sameSymbol):
    print("right")
else:
    print("wrong")
    
        
        
    
    
    
    

