# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:52:55 2022

@author: Asus
"""

# minimax algo here:
# def minimax()

import turtle



screen = turtle.Screen()

screen.bgcolor('lightblue')

x = screen.numinput("Enter distance:",100)

player = turtle.Turtle()

player.color('blue')

player.shape('turtle')

# print(player.size())

ai = player.clone()

ai.color('red')



player.penup()

player.goto(-350, 100)

ai.penup()

ai.goto(350, 100)

true = 1

# x = screen.numinput("Enter distance:",100)

x+=1

stepsize = 700/x

line = turtle.Turtle()

line.penup()

line.goto(-350,80)

base = turtle.Turtle()

base.penup()

base.goto(350, 80)

# line.pendown()

xx = 20

mm = int(x+1)

for i in range(mm):
    line.pendown()
    line.forward(xx)
    line.penup()
    line.forward(stepsize-xx)
        
while true == 1:

    steps = screen.numinput("Enter steps:",100)
    
    player.forward(stepsize*steps)
    if(player.pos()==ai.pos()):
        screen.title("Player lost the game!")
        break
    if(player.pos()>ai.pos()):
        screen.title("Player won the game!")
        break
    
    # from minimax:
    # steps_ai = minimax()
    
    steps_ai = screen.numinput("Enter steps:",100)
    
    ai.backward(steps_ai*stepsize )
    if(player.pos()==ai.pos()):
        screen.title("Player lost the game!")
        break
    if(player.pos()>ai.pos()):
        screen.title("Player won the game!")
        break
    
    

turtle.done()