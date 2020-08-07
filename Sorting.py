# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:29:26 2020

@author: shaurya
"""


def bubblesort(a):
    n = len(a)
    
    for i in range(n):
        for j in range(0,n-1):
            if(a[j]>a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1]=tmp


a = [7,6,3,4,2,1]
bubblesort(a)

for i in a:
    print(i)
             
