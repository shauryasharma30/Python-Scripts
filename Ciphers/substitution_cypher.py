# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:18:49 2020

@author: shaurya
"""


import string
dict={}
data=""
file = open("cypher.txt","w")

for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=[string.ascii_letters[i-1]]
print(dict)

with open ("sample.txt") as f:
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data = dict[c]
        else:
            data = c
        file.write("".join(data))
        #print(data)

file.close()        
    