# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:47:00 2020

@author: shaurya
"""
import random

def choose():
    words=["rainbow","encyclopedia","swimming","hollywood","metallica","deleterious","imperative","secondary"]
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(pn1,pn2,p1,p2):
    print(pn1,"your score is",p1)
    print(pn2,"your score is",p2)
    
    

def play():
    player1 = input("player 1 enter your alias ")
    player2 = input("player 2 enter your alias ")
    p1 = 0
    p2 = 0
    turn = 1
    while(1):
        picked_word = choose()
        question = jumble(picked_word)
        print("your word is",question)
        #player 2
        if turn%2==0:
            print(player2,"your turn")
            ans = input("your answer:")
            if ans==picked_word:
                p2 +=1
                print(player2,"your score is :",p2)
            else:
                print("sorry but you didnt get that right")
                c = input("to continue press 1 and to quit 0:")
                if c=='0':
                    thank(player1,player2,p1,p2)
                    break
        #player 1        
        else:
             print(player1,"your turn")
             ans = input("your answer:")
             if ans==picked_word:
                p1 +=1
                print(player1,"your score is :",p1)
             else:
                print("sorry but you didnt get that right")
                c = input("to continue press 1 and to quit 0:")
                if c=='0':
                    thank(player1,player2,p1,p2)
                    break
        turn = turn+1            
        
        
    






play()