import turtle
import time
import random

delay=0.1

#setup the screen
wn=turtle.Screen()
wn.title("My Snake game at Mumbi")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

#set the snakes head
head=turtle.Turtle()
head.shape("square")
head.speed(0)
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"
# Snake food
food=turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("red")
food.penup()
food.goto(0,100)


segments=[]






#functions
def go_up():
    head.direction="up"
    
def go_down():
    head.direction="down"
    
def go_left():
    head.direction="left"
    
def go_right():
     head.direction="right"
    
   
    
def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
        
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
	
	
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
	
	
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
#keyboard bindings
wn.listen()
wn.onkeypress(go_up ,"u")
wn.onkeypress(go_down ,"d")
wn.onkeypress(go_left ,"l")
wn.onkeypress(go_right ,"r")

	
	
while True:
    wn.update()
    #check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()< -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        #Clear the segments list
        segments.clear()

    
    

#Check for collision of food
    if head.distance(food)<20:
        #move the food to a random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("grey")
        new_segment.penup()
        new_segment.shape("square")
        segments.append(new_segment)
#Move the end segents first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #Move segment 0  to where the head is
    if  len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
        
        
    move()
    time.sleep(delay)
     
	 
wn.mainloop()
	







