# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:55:14 2015

@author: Arthur
"""

import turtle
import random
import time

from unicodedata import normalize        #para tornar as palavras da lista "normais"
def formatar(txt):
    return normalize('NFKD',txt).encode('ASCII','ignore').decode('ASCII')
    
if __name__ == '__main__':
    from doctest import testmod
    testmod()
  
#-----------------------------------------------------------------------------------------------------

rights = 0     #número inicial de acertos
wrongs = 0      #número inicial de erros
used = []       #lista para se colocar as letras(guess) já computadas
victory = 0     #número de vitórias
defeat = 0       #número de derrotas


t = turtle.Turtle()
t.speed(10)

turtle1 = turtle.Turtle()
turtle1.speed(10)

turtle2 = turtle.Turtle()
turtle2.speed(10)


tartaruga = turtle.Turtle()
tartaruga.speed(10)


tartaruga2 = turtle.Turtle()
tartaruga2.speed(10)

tartaruga3 = turtle.Turtle()
tartaruga3.speed(10)


tartaruga4 = turtle.Turtle()
tartaruga4.speed(10)


tartaruga4 = turtle.Turtle()
tartaruga4.speed(10)


tartaruga5 = turtle.Turtle()
tartaruga5.speed(10)


tartaruga5 = turtle.Turtle()
tartaruga5.speed(10)


tartaruga6 = turtle.Turtle()
tartaruga6.speed(10)


tartaruga7 = turtle.Turtle()
tartaruga7.speed(10)

tartaruga8 = turtle.Turtle()
tartaruga.speed(10)
tartaruga8.shape("turtle")

#-------------------------------------------------------------------------------------------------



def draw_spaces():        #desenha as linhas para as palvras
    print("draw_spaces")
    turtle1.shape("turtle")
    
    for i in range(len(secret_word)):
        if secret_word == " ":
            turtle1.penup()
            turtle1.setpos((-310+i *30,-265))
            turtle1.write(" ",False,font = ("Arial",15))
            turtle1.hideturtle()

        elif secret_word[i] == " ":
            turtle1.penup()
            turtle1.setpos((-310+i *30,-265))
            turtle1.write(" ",False,font = ("Arial",15))
            turtle1.hideturtle()
        else:
            turtle1.penup()
            turtle1.setpos((-310+i *30,-265))
            turtle1.write("_",False,font = ("Arial",15))
            turtle1.hideturtle()

def PlayAgain():    #função para perguntar se usuário quer recomeçar o jogo
    turtle.setpos(-250,0)                      
    resposta = turtle.textinput("Jogo da Forca","Jogar de novo?")
    if resposta.isalpha() and len(resposta) > 0:
        if resposta == "sim" or resposta == "SIM" or resposta == "Sim":
            print("a")
            turtle.clear()
            turtle1.clear()
            turtle2.clear()
           
            t.clear()
            tartaruga.clear()
            tartaruga2.clear()
            tartaruga3.clear()
            tartaruga4.clear()
            tartaruga5.clear()
            tartaruga6.clear()
            tartaruga7.clear()
            turtle.resetscreen()
                      
            window.clearscreen
            jogo = True
#------------------------------------------------------------------------------------------------------------                        
    
        elif resposta == "não" or resposta == "Não" or resposta == "NÃO":
            
            GameOver()     #fim de jogo
    
            t.clear()
            turtle2.clear()
            tartaruga.clear()
            tartaruga2.clear()
            tartaruga3.clear()
            tartaruga4.clear()
            tartaruga5.clear()
            tartaruga6.clear()
            tartaruga7.clear()
            
            window.clearscreen()
            jogo == False
            
#------------------------------------------------------------------------------------------------------------------------------                    
def YouWin():      #comando para dar um "You Win" na tela
    
    turtle1.setpos(-1500,50)
    turtle1.write("You won!", move=False, align="left", font=("Arial", 30, "normal"))
    time.sleep(1)
    turtle1.clear()
    turtle1.hideturtle()
 
def GameOver():    #comando para dar um print na tela "Game Over"
    turtle1.setpos(-150,50)
    
    turtle1.write("Game Over", move=False, align="left", font=("Arial", 30, "normal"))
    turtle1.hideturtle()

def Scoreboard():     #Placar
    t.penup()
    t.setpos(150,50)
    t.pendown()
    t.write("vitórias: %d" % (victory), move=False, align="left", font=("Arial",20, "normal"))
    t.penup()
    t.setpos(150,-30)
    t.write("derrotas: %d" % (defeat), move=False, align="left", font=("Arial",20, "normal"))
    t.hideturtle() 
def ChutesMedia():     #Chutes/palavra
    Media = len(used) / victory + defeat
    return Media
    tartaruga8.penup
    tartaruga8.setpos(150,-250)
    tartaruga8.write("chutes/palavras: %d" % (Media), move=False, align="left", font=("Arial",20, "normal"))
    
#----------------------------------------------------------------------------------------------

def forca():          #fazer a forca
    window = turtle.Screen()   
    window.bgcolor("yellow")
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
    tartaruga2.color("blue")    
    tartaruga2.speed(10)
    tartaruga2.penup()
    tartaruga2.setpos(-300,110)
    
    
    tartaruga2.pendown()
    for i in range (1):
        tartaruga2.circle(50)
        tartaruga2.heading()
        tartaruga2.penup()
        tartaruga2.hideturtle()

        
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
        tartaruga3.hideturtle()

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
        tartaruga4.hideturtle()
    
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
        tartaruga5.hideturtle()
  
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
        tartaruga6.hideturtle() 
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
        tartaruga7.hideturtle()

#-----------------------------------------------------------------------------------------------------

file = open("entrada.txt", encoding = "utf - 8")    #Abrir a lista com as palavras
lista = file.readlines()
jogo = True
while jogo == True:        #condição para o jogo enquanto estiver True
    #MediaPalavra()
    Scoreboard()
    window = turtle.Screen()    
    window.bgcolor("white")
    window.setup(width=1500,height =700, startx = 0,starty=0)
    
    a = random.choice(lista)     #escolha aleatória da palavra secreta
    secret_word2 = formatar(a)
    secret_word = secret_word2.lower()
    secret_word = secret_word.strip()     #tornar as letras sem acento e minúsculas
    
    b = secret_word.count(" ")
    lista.remove(a)        #remover a palavra secreta escolhida da lista, para não repeti-la se jogador querer continuar com o jogo
    
    forca()
    draw_spaces()
    
    if b > 0:
        rights = rights + b    #no caso de uma polavra tiver espaços, este será contado já 
    
    while wrongs != 6 and rights != len(secret_word):    
        print("rights ", rights)
     
        print(secret_word)
        guess = turtle.textinput("Jogo da Forca","Guess a letter")
        
        if len(guess) > 0 and guess.isalpha():
            
            if guess in used:         #quando se digitar uma letra que já foi usada
                turtle2.setpos(-150,25)
                turtle2.write("Already used", move=False, align="left", font=("Arial",35, "normal"))
                time.sleep(1)
                turtle2.clear()
                turtle2.hideturtle()
            elif guess in secret_word:
                turtle.penup()
                turtle.setpos(0,0)
                used.append(guess)    #adicionar a letra(guess) numa lista(used)
               
                for i in range(len(secret_word)):  #desenhar a letra se esta for a correta
                    
                    if guess == secret_word[i]:       #substitui para a escrita da palavra normas=l(com acentos e maiúsculas)
                        rights += 1
                        turtle.setpos(i *30 - 305, - 265)
                        
                        
                        turtle.pendown()
                        turtle.write(a[i], True, align="center",font = ("Arial",15,"normal"))
                        turtle.penup()
                        turtle.hideturtle()
           
                    
                    
                    
#-------------------------------------------------------------------------------------------------------------------------            
            elif guess not in secret_word:
                turtle2.setpos(-150,25)
                
                turtle2.write("Wrong", move=False, align="left", font=("Arial",35, "normal"))
                time.sleep(1)
                turtle2.clear()
                turtle2.hideturtle()
                
                wrongs += 1       #contagem de erro
                used.append(guess)   #adicionar a letra na lista 'used'
                
            
                    
                if wrongs < 6:           #condições do número de erros
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
            
                
        t.penup()  
        t.setpos(100,150)
        t.pendown()            
        t.write(used, move=False, align="left", font=("Arial",25, "normal"))     
        t.hideturtle
        
                
    if rights == len(secret_word):
        rights = 0
        wrongs = 0
        del used[:]
        i = 0
        YouWin()
        victory += 1
        ChutesMedia()
        PlayAgain()
        
        
    elif wrongs == 6:
        rights = 0
        wrongs = 0
        del used[:]
        i = 0
        leg2()
        GameOver()                 
        defeat +=1
        ChutesMedia()
        PlayAgain()
#--------------------------------------------------------------------------------------------------------------                             
    t.penup()  
    t.setpos(100,150)
    t.pendown()            
    t.write(used, move=False, align="left", font=("Arial",25, "normal"))          # escrever as letras já usadas durante o jogo
    t.hideturtle
        
                

        
      
turtle.exitonclick()                        