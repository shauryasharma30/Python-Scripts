# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:11:52 2020

@author: shaurya
"""

import random

doors=[0]*3
goatdoors=[0]*2
swap = 0
dont_swap = 0
j=0
while(j<3):
    x = random.randint(0,2)
    doors[x] = "TREASURE"
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="GOAT"
            goatdoors.append(i)
    choice = int(input("Enter your door number 0/1/2 : "))
    door_open = random.choice(goatdoors) 
    while (door_open==choice):
        door_open = random.choice(goatdoors)
    ch = input("Do yo want to swap ? y/n:")
    if(ch=='y'):
        if(doors[choice]=="GOAT"):
            print("YOU WIN THE TREASURE")
            swap= swap+1
        else:
            print("YOU LOSE")
    else:
        if(doors[choice]=="GOAT"):
            print("YOU LOSE")
        else:
            print("YOU WIN THE TREASURE")
            dont_swap= dont_swap+1
    j=j+1        
        
print(swap,"swap wins")
print(dont_swap,"unswapped wins")        
         
        
        
    
    
            
            