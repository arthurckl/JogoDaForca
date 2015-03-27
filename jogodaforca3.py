# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:24:15 2015

@author: Arthur
"""
import turtle
import random
import time
used = ["o"]
rights = 0
wrongs = 0
words_used = []

#mecanismo para as tentativas

file = open("entrada.txt", encoding = "utf - 8")    #Abrir a lista
lista = file.readlines()
 
window = turtle.Screen()   
window.bgcolor("white")
t = turtle.Turtle()
t.speed(10)

secret_word = random.choice(lista)     #escolha aleatória da palavra secreta
a = 0
x = len(secret_word)
print(x)
print (secret_word)
def draw_spaces():
    t.penup()

    t.setheading(0)    
    t.setpos(-530,-300)
    for i in range(len(secret_word)):
        t.pendown()
        t.forward(50)
        t.penup()
        t.forward(10)


def draw_letter(guess):
    t.penup()
    t.setheading(0)
    
    for i in range(1):
        t.pendown()
        t.write(guess, True, align="center", font = ("Arial", 35, "normal"))
        t.penup()
    return draw_letter()

def head():
    pass

def body():
    pass

def arm1():
    pass

def arm2():
    pass

def leg1():
    pass
def leg2():
    pass
draw_spaces()

def guess1():
     guess = turtle.textinput("Jogo da Forca","Guess a letter")
    


while wrongs < 6:
    
    guess = turtle.textinput("Jogo da Forca","Guess a letter")
    

    if len(guess) <= 1 and len(guess) > 0 and guess.isalpha():
        
        
        
        
        if guess in secret_word:
            turtle.hideturtle()
            turtle.penup()
            turtle.setpos(0,0)
            used.append(guess)
            
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    
                    
                    turtle.setpos(i * 60 -505, - 265)
                    
                    
                    for i in range(1):
                        turtle.pendown()
                        turtle.write(guess, True, align="center",font = ("Arial",35,"normal"))
                        turtle.penup()
        
        elif guess not in secret_word:
            turtle.setpos(-200,0)
            turtle.write("Wrong", move=False, align="left", font=("Arial", 50, "normal"))
            
            wrongs += 1
            used.append(guess)
            
            
                
            if wrongs < 6:
                if wrongs == 1:
                    head()
                elif wrongs == 2:
                    body()
                elif wrongs == 3:
                    arm1()
                elif wrongs == 4:
                    arm2()
                elif wrongs == 5:
                    leg1()
                     
                           
        elif guess in used:
            turtle.setpos(-250,0)
            turtle.write("Already used", move=False, align="left", font=("Arial", 50, "normal"))
                                                         
                     
                    
def GameOver():
    turtle.setpos(-250,0)
    
    turtle.write("Game Over", move=False, align="left", font=("Arial", 50, "normal"))
    time.sleep(3)
    turtle.clear()
    
def PlayAgain():
    turtle.setpos(-250,0)
    resposta = turtle.textinput("Jogo da Forca","Jogar de novo?")
    if resposta.isalpha() and len(resposta) > 0:
        if resposta == sim or resposta == SIM or resposta == Sim:
            guess()
        elif resposta == não or resposta == Não or resposta == NÃO:
            GameOver()
            
        






if wrongs == 6:
    GameOver()    
    PlayAgain()



print(used)        
        
    
    
    






window.exitonclick()