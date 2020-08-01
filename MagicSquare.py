# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:45:10 2020

@author: shaurya
"""


def magicSquare(n):
    magic=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magic.append(l)
        
    i = n//2
    j = n-1
    count = 1
    num = n*n
    
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magic[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magic[i][j]=count
            count+=1
        i = i-1
        j = j+1
        
    for i in range(n):
        for j in range(n):
            print(magic[i][j],end=" ")
        print() 
        
        
    print("the sum of each row/column/diagonal is",str(n*(n**2+1)/2)) 
      
          
c = input("input the magic sqaure number: ")          
n = int(c)
magicSquare(n)              

          
          
          
          
          
          
          

          
          
          
