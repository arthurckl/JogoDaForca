# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:34:34 2015

@author: Arthur
"""
import turtle


letter = window.screeninput("letter: ")


def forca():          #fazer a forca
    window = turtle.Screen()   
    window.bgcolor("white")
    window.title("Jogo da Forca")
    tartaruga = turtle.Turtle()
    tartaruga.speed(10)
    tartaruga.penup()
    tartaruga.setpos(-600,-300)
    tartaruga.color("black")
    tartaruga.pendown()
    for i in range (1):
        tartaruga.forward(300)
        tartaruga.backward(150)
        tartaruga.left(90)
        tartaruga.forward(600)
        tartaruga.right(90)
        tartaruga.forward(150)
        tartaruga.right(90)
        tartaruga.forward(90)    
        tartaruga.right(90)
        tartaruga.forward(75)    
        tartaruga.backward(150)
        tartaruga.forward(75)
        tartaruga.penup()

def head():       #forca
    tartaruga2 = turtle.Turtle()
    tartaruga2.speed(10)
    tartaruga2.penup()
    tartaruga2.setpos(-300,110)
    tartaruga2.color("red")
    tartaruga2.pendown()
    for i in range (1):
        tartaruga2.circle(50)
        tartaruga2.heading()
        tartaruga2.penup()
        
def body():        #corpo
    tartaruga3 = turtle.Turtle()
    tartaruga3.speed(10)
    tartaruga3.penup()
    tartaruga3.setpos(-300,110)
    tartaruga3.color("red")
    tartaruga3.pendown()
    for i in range (1):
        tartaruga3.right(90)
        tartaruga3.forward(200)
        tartaruga3.penup()

def arm1():          #braço
    tartaruga4 = turtle.Turtle()
    tartaruga4.speed(10)
    tartaruga4.penup()
    tartaruga4.setpos(-300,10)
    tartaruga4.color("red")
    tartaruga4.pendown()
    for i in range (1):
        tartaruga4.right(45)
        tartaruga4.forward(100)
        tartaruga4.penup()
    
def arm2():            #braço
    tartaruga5 = turtle.Turtle()
    tartaruga5.speed(10)
    tartaruga5.penup()
    tartaruga5.setpos(-300,10)
    tartaruga5.color("red")
    tartaruga5.pendown()
    for i in range (1):
        tartaruga5.right(135)
        tartaruga5.forward(100)
        tartaruga5.penup()
  
def leg1():         #braço
    tartaruga6 = turtle.Turtle()
    tartaruga6.speed(10)
    tartaruga6.penup()
    tartaruga6.setpos(-300,-90)
    tartaruga6.color("red")
    tartaruga6.pendown()
    for i in range (1):
        tartaruga6.right(45)
        tartaruga6.forward(100)
         
def leg2():              #perna
    tartaruga7 = turtle.Turtle()
    tartaruga7.speed(10)
    tartaruga7.penup()
    tartaruga7.setpos(-300,-90)
    tartaruga7.color("red")
    tartaruga7.pendown()
    for i in range (1):
        tartaruga7.right(135)
        tartaruga7.forward(100)
        
while wrongs < 6 :           #desenha os erros
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
if wrongs == 6:
    leg2()
    print ("Game Over")

    






















