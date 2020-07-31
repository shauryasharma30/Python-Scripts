# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:19:18 2020

@author: shaurya
"""

def fizzBuzz(r):
        for i in range(1,r):
         if(i%3 == 0 and i%5 ==0):
             print(i,"fizzbuzz")
         else:
              if(i%5 == 0):
               print(i,"buzz")
              else:
                   if(i%3 == 0):
                    print(i,"fizz")
                   else:
                     print(i)
             
fizzBuzz(51)                