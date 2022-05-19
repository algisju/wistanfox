#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  turtlet.py
#  
#  Copyright 2021 geek <geek@KALIBOX>
#  
#  
from turtle import *
color('red', 'yellow')
bgcolor("Black")
title("God Damn Turtle")
shape('circle')
shapesize(0.1,0.1,0)
pu()
goto(-300,200)
color('white')
write('YI-HAA!!', True, align="center",font=('Arial',96,'bold'))
color('green')
goto(0,0)
pd()
pensize(2)
speed(0)
#begin_fill()
while True:
	forward(500)
	now=pos()
	pu()
	#goto(pos())
	#goto(now)
	print(now)
	pd()
	circle(5)
	left(170)
	write(str(pos()),False,align='center',font=('Arial',8,'normal'))
	if abs(pos()) < 1:
		break
end_fill()
done()

# def drawthings():
	# s =	turtle.Screen()
	# s.bgcolor("black")
	# t = turtle.Turtle

	# for i in range(4):
		# t.forward(350)
		# t.right(90)
	# turtle.done()

# def main(args):
	# drawthings()
	# return 0

# if __name__ == '__main__':
    # import sys
    # sys.exit(main(sys.argv))
