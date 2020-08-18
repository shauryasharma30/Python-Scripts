# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:34:09 2020

@author: shaurya
"""
import turtle
from random import randint
turtle.bgcolor("black")
pen = turtle.Turtle()

width = 5
height =5
dot_distance = 25

pen.setpos(-250, 250)
pen.penup()
list_color = ["white","red","yellow","blue","green","voilet"]

def spiral(m,n):
    k=0 #k is starting index for row
    l=0 #l is starting index for column
    f=0
    pen.color("white")
    col = randint(0,5)
    pen.color(list_color[col])
    
    while(k<m and l<n):
        
        if(f==1):
            pen.right(90)
        #printing first row
        for i in range(l,n):
            pen.dot()
            pen.forward(dot_distance)
           #print(a[k][i],end=" ")
        
        #printing last column except the first element of that last row
        k+=1
        f=1
        pen.right(90)
        col = randint(0,5)
        pen.color(list_color[col])
        for i in range(k,m):
            pen.dot()
            pen.forward(dot_distance)
           # print(a[i][n-1],end=" ")
        
        n-=1
        pen.right(90)
        col = randint(0,5)
        pen.color(list_color[col])
        if(k<m):
            #printing last row 
            for i in range(n-1,l-1,-1):
                pen.dot()
                pen.forward(dot_distance)
                #print(a[m-1][i],end=" ")
                
            m-=1
        pen.right(90)
        col = randint(0,5)
        pen.color(list_color[col])
        if(l<n):
            #printing the first column
            for i in range(m-1,k-1,-1):
                pen.dot()
                pen.forward(dot_distance)
                #print(a[i][l],end=" ")
            l+=1

    
spiral(20,20)            
turtle.done()        
    