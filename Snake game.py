import turtle
import time
import random

screen = turtle.Screen()
screen.title("  SNAKE GAME BY KRISH")
screen.setup(width=700,height=700)
screen.tracer(0)
turtle.bgcolor=("#0E7283")

#BORDER
turtle.speed(5)
turtle.pensize(5)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("red")

turtle.forward(600)
turtle.right(90)

turtle.forward(500)
turtle.right(90)

turtle.forward(600)
turtle.right(90)

turtle.forward(500)
turtle.penup()

turtle.hideturtle()

score = 0
delay = 0.1

#SNAKE
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#FOOD
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("orange")
food.penup()
food.goto(30,30)

old_food=[]

#SCORING
scoring = turtle.Turtle()
scoring.speed(0)
scoring.shape("turtle")
scoring.color("green")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score:",align="center",font=("Verdana",25,"bold"))

def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"
    
def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)

#EVENTS
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

#main logic
while True:
    screen.update()

    #snake colliding w food
    if snake.distance(food) < 20:
        x = random.randint(-290,270)
        y = random.randint(-240,240)
        food.goto(x,y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score),align="center",font=("Verdana",25,"bold"))
        delay -= 0.001

        new_food = turtle.Turtle()
        new_food.shape("square")
        new_food.color("green")
        new_food.penup()
        old_food.append(new_food)

    for index in range (len(old_food)-1,0,-1):
        a=old_food[index-1].xcor()
        b=old_food[index-1].ycor()
        old_food[index].goto(a,b)
    if len(old_food)>0:
        a = snake.xcor()
        b = snake.ycor()
        old_food[0].goto(a,b)
    snake_move()

    if snake.xcor()>280 or snake.xcor() <-300 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(2)
        screen.clear()
        screen.bgcolor("red")
        scoring.goto(0,0)
        scoring.write("GAME OVER \n Score:{}".format(score),align="center",font=("Verdana",25,"bold"))

    for i in old_food:
        if i.distance(snake) < 20:
            time.sleep(2)
            screen.clear()
            screen.bgcolor("red")
            scoring.goto(0,0)
            scoring.write("GAME OVER \n Score:{}".format(score),align="center",font=("Verdana",25,"bold"))
    
    time.sleep(delay)

turtle.Terminator()