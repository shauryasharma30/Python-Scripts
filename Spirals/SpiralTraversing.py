# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:45:54 2020

@author: shaurya
"""

def spiral(m,n,a):
    k=0 #k is starting index for row
    l=0 #l is starting index for column
    
    while(k<m and l<n):
        
        #printing first row
        for i in range(l,n):
            print(a[k][i],end=" ")
        
        #printing last column except the first element of that last row
        k+=1
        for i in range(k,m):
            print(a[i][n-1],end=" ")
        
        n-=1
        
        if(k<m):
            #printing last row 
            for i in range(n-1,l-1,-1):
                print(a[m-1][i],end=" ")
                
            m-=1
        
        if(l<n):
            #printing the first column
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=" ")
            l+=1

a = []
count = 1
for i in range(4):
    l =[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
    
spiral(4, 4, a)            
        
    
    
    
    
    