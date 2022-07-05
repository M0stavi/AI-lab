# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:52:55 2022

@author: Asus
"""

# minimax algo here:
# def minimax()

import turtle
import numpy as np

def close():
    exit()

def take_zero(a,b,c,d,distance):
    lst =[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.append(d)
    lst = sorted(lst)
    #print(lst)
    a = lst[0]
    b = lst[1]
    c = lst[2]
    d = lst[3]
    
    if a[0] == distance or b[0] == distance or c[0] == distance or d[0] == distance :
        if a[0] == distance:
            a=(a[0],True)
            return a
        
        elif b[0] == distance:
            b=(b[0],True) 
            return b
        
        elif c[0] == distance:
            c=(c[0],True)
            return c
        
        elif d[0] == distance:
            d=(d[0],True)
            return d
        
        
    else:
        if a[1]:
            return a
        
        elif b[1]:
            return b
        
        elif c[1]:
            return c
        
        elif d[1]:
            return d
        
        return a
    
    
def avoid_zero(a,b,c,d,distance):
    
    lst =[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.append(d)
    lst = sorted(lst)
    a = lst[0]
    b = lst[1]
    c = lst[2]
    d = lst[3]
    
    #print(lst)
    if (a[0] > distance or b[0] > distance or c[0] > distance or d[0] > distance):
        if a[0] > distance:
            return a
        elif b[0] > distance :
            return b
        elif c[0] > distance :
            return c
        elif d[0] > distance :
            return d
        
    else:
        if a[1]==False:
            return a
        elif b[1]==False :
            return b
        elif c[1]==False :
            return c
        elif d[1]==False:
            return d
    return a

def minimax (policeTurn, step_flag , distance):
    step = step_flag[0]
    flag = step_flag[1]
    distance -= step
	# base case : targetDepth reached
    if distance <= 0:
        return step_flag
    two = 2
    three = 3
    four = 4
    five =5
    if policeTurn : 
        #print("Before Police" , step, distance)
        #flag = False
        step_flag = take_zero(minimax(False, (two, flag) ,distance),	
                         minimax(False, (three, flag) ,distance),
                     	minimax(False, (four, flag),distance),
                     	minimax(False, (five, flag) ,distance),distance)
        
        #print("After Police" , step_flag, distance)
        return step_flag

    else:
        #print("Before Theif" , step, distance)
        #flag= False
        step_flag = avoid_zero(minimax(True, (two, flag) ,distance),	
                         minimax(True, (three, flag) ,distance),
                     	minimax(True, (four, flag),distance),
                     	minimax(True, (five, flag) ,distance),distance)
		#step = avoid_zero(minimax(True, 2,distance), minimax(True, 3 ,distance),minimax(True,4,distance),minimax(True, 5,distance),distance)
        #print("After Theif" , step_flag, distance)
        return step_flag

screen = turtle.Screen()

screen.title("")

# screen.bgcolor('lightblue')

screen.bgpic("proj.gif")

# x = screen.numinput("Enter distance:",100)

screen.title("Level 1")

x = 7

# x = np.array([7,15,23],np.int32)

dist = x+1

player = turtle.Turtle()

player.color('blue')

player.shape('turtle')

# print(player.size())

ai = player.clone()

ai.color('red')

player.penup()

player.goto(-350, 300)

ai.penup()

ai.goto(350, 300)

true = 1

# x = screen.numinput("Enter distance:",100)

x+=1

stepsize = 700/x

line = turtle.Turtle()

line.penup()

line.goto(-350,280)

# base = turtle.Turtle()

# base.penup()

# base.goto(350, 280)

# line.pendown()

xx = 20

mm = int(x+1)

str = "abc"

win = 0    

for i in range(mm):
    line.pendown()
    line.forward(xx)
    line.penup()
    line.forward(stepsize-xx)
    
# for i in range(3):
#     dist = x[i]+1
    
    
while(dist>0):
    steps = screen.numinput("Steps:","Enter valid steps(2/3/4/5)")
    
    if steps != 2 and steps != 3 and steps != 4 and steps != 5:
        continue
    
    player.forward(stepsize*steps)
    
    dist-=steps 
    
    if(dist == 0):
        # screen.title("Player lost the game!")
        str = "Player lost the game!"
        win=0
        break
    
    if(dist<0):
        # screen.title("Player won the game!")
        str = "Player won the game!"
        win=1
        break
    
    # player.forward(stepsize*steps)
    # if(player.pos()==ai.pos()):
    #     screen.title("Player lost the game!")
    #     break
    # if(player.pos()>ai.pos()):
    #     screen.title("Player won the game!")
    #     break
    
    # steps_ai = screen.numinput("Enter steps:",100)
    
    # tem = minimax (True, (steps,False) , dist)
    
    # steps_ai = tem[0]
    
    tem = minimax (True, (steps,False) , dist+steps)
    
    steps_ai = tem[0]
    
    dist-=steps_ai
    
    ai.backward(steps_ai*stepsize )
    
    if(dist == 0):
        # screen.title("Player lost the game!")
        str = "Player lost the game!"
        win=0
        break
    
    if(dist<0):
        # screen.title("Player won the game!")
        str = "Player won the game!"
        win=1
        break
    
    
    # ai.backward(steps_ai*stepsize )
    # if(player.pos()==ai.pos()):
    #     screen.title("Player lost the game!")
    #     break
    # if(player.pos()>ai.pos()):
    #     screen.title("Player won the game!")
    #     break
    
    # dist-=steps
    
    # dist-=steps_ai

    
    
        
# while true == 1:

#     steps = screen.numinput("Enter steps:",100)
    
#     player.forward(stepsize*steps)
#     if(player.pos()==ai.pos()):
#         screen.title("Player lost the game!")
#         break
#     if(player.pos()>ai.pos()):
#         screen.title("Player won the game!")
#         break
    
#     # from minimax:
#     # steps_ai = minimax()
    
#     steps_ai = screen.numinput("Enter steps:",100)
    
#     ai.backward(steps_ai*stepsize )
#     if(player.pos()==ai.pos()):
#         screen.title("Player lost the game!")
#         break
#     if(player.pos()>ai.pos()):
#         screen.title("Player won the game!")
#         break
    
    

# turtle.done()

# turtle.delay(3000)

# for i in range(100000):
#     print("hello")

if win != 0:

    ex = turtle.textinput(str,"Continue to level 2(yes/no)?")

if win == 0:
    ex = "no"
    screen.title("Player lost the game!")

if ex[0] == 'y':
    

    screen.title("Level 2")
    
    x = 15
    
    dist = x+1
    
    player.penup()
    
    player.goto(-350, 100)
    
    ai.penup()
    
    ai.goto(350, 100)
    
    true = 1
    
    x+=1

    stepsize = 700/x

    line = turtle.Turtle()

    line.penup()

    line.goto(-350,80)
    
    xx = 20

    mm = int(x+1)

    str = "abc"

    win = 0    

    for i in range(mm):
        line.pendown()
        line.forward(xx)
        line.penup()
        line.forward(stepsize-xx)
        
    while(dist>0):
        steps = screen.numinput("Steps:","Enter valid steps(2/3/4/5)")
        
        if steps != 2 and steps != 3 and steps != 4 and steps != 5:
            continue
        
        player.forward(stepsize*steps)
        
        dist-=steps 
        
        if(dist == 0):
            # screen.title("Player lost the game!")
            str = "Player lost the game!"
            win=0
            break
        
        if(dist<0):
            # screen.title("Player won the game!")
            str = "Player won the game!"
            win=1
            break
        
        # player.forward(stepsize*steps)
        # if(player.pos()==ai.pos()):
        #     screen.title("Player lost the game!")
        #     break
        # if(player.pos()>ai.pos()):
        #     screen.title("Player won the game!")
        #     break
        
        # steps_ai = screen.numinput("Enter steps:",100)
        
        # tem = minimax (True, (steps,False) , dist)
        
        # steps_ai = tem[0]
        
        tem = minimax (True, (steps,False) , dist+steps)
        
        steps_ai = tem[0]
        
        dist-=steps_ai
        
        ai.backward(steps_ai*stepsize )
        
        if(dist == 0):
            # screen.title("Player lost the game!")
            str = "Player lost the game!"
            win=0
            break
        
        if(dist<0):
            # screen.title("Player won the game!")
            str = "Player won the game!"
            win=1
            break
        
        
if win != 0:

    ex = turtle.textinput(str,"Continue to level 3(yes/no)?")

if win == 0:
    ex = "no"
    screen.title("Player lost the game!")

if ex[0] == 'y':
    

    screen.title("Level 3")
    
    x = 25
    
    dist = x+1
    
    player.penup()
    
    player.goto(-350, -230)
    
    ai.penup()
    
    ai.goto(350, -230)
    
    true = 1
    
    x+=1

    stepsize = 700/x

    line = turtle.Turtle()

    line.penup()

    line.goto(-350,-240)
    
    xx = 20

    mm = int(x+1)

    str = "abc"

    win = 0    

    for i in range(mm):
        line.pendown()
        line.forward(xx)
        line.penup()
        line.forward(stepsize-xx)
        
    while(dist>0):
        steps = screen.numinput("Steps:","Enter valid steps(2/3/4/5)")
        
        if steps != 2 and steps != 3 and steps != 4 and steps != 5:
            continue
        
        player.forward(stepsize*steps)
        
        dist-=steps 
        
        if(dist == 0):
            # screen.title("Player lost the game!")
            str = "Player lost the game!"
            win=0
            break
        
        if(dist<0):
            # screen.title("Player won the game!")
            str = "Player won the game!"
            win=1
            break
        
        # player.forward(stepsize*steps)
        # if(player.pos()==ai.pos()):
        #     screen.title("Player lost the game!")
        #     break
        # if(player.pos()>ai.pos()):
        #     screen.title("Player won the game!")
        #     break
        
        # steps_ai = screen.numinput("Enter steps:",100)
        
        # tem = minimax (True, (steps,False) , dist)
        
        # steps_ai = tem[0]
        
        tem = minimax (True, (steps,False) , dist+steps)
        
        steps_ai = tem[0]
        
        dist-=steps_ai
        
        ai.backward(steps_ai*stepsize )
        
        if(dist == 0):
            # screen.title("Player lost the game!")
            str = "Player lost the game!"
            win=0
            break
        
        if(dist<0):
            # screen.title("Player won the game!")
            str = "Player won the game!"
            win=1
            break
    

ex = screen.textinput(str,"Press any character(a-z)")

if ex != "":
    turtle.bye()