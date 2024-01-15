import turtle

import os
wn = turtle.Screen()
wn.setup(width=950, height=800)
wn.tracer()
wn.bgcolor("white")
# game loop

# score
player_a_score = 0
player_b_score = 0

# volley
volley_ = 0
pausedx = 0

# objects

# paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-440, 0)
paddle_a.color("red")

# paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("pink")
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(440, 0)

# ball

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(1.25)
ball.goto(0, 0)
ball.dx = 2
ball.dy = 1
ball.fx = 1
ball.penup()
ball.speed(0)

# pen

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed()
pen.setpos(0, 300)
pen.write("Player A:0 Player B:0 Volley:0",align="center", font=("Courier", 16, "normal"))


dypen = turtle.Turtle()
dypen.hideturtle()
dypen.up()
dypen.speed()
dypen.setpos(0,-350)
dypen.write("({},{})".format(ball.dx, ball.dy),align="center", font=("Courier", 16, "normal"))

# functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def pause():

    ball.dy *= 0
    ball.dx *= 0

def resume():
    if ball.dy == 0:
        ball.dy += 1
    if ball.dx == 0:
        ball.dx += 2
    elif pausedx <= 0:
        ball.dx += -2
    dypen.clear()
    dypen.write("({},{})".format(ball.dx, ball.dy),align="center", font=("Courier", 16, "normal"))
# keybindings

wn.listen()
wn.onkey

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(pause, "Escape")
wn.onkeypress(resume, "space")

# game_loop
while True:
    wn.update()

    # ball_movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball speed

    #set max x variable speed
    if ball.dx == -64:
        ball.dx += 32
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    if ball.dx == 64:
        ball.dx -= 32
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))

    # hit! Speed up dx times 2 each hit, set ball dy direction
    if ball.xcor() == 416 and ball.ycor() > paddle_b.ycor() - 57 and ball.ycor() < paddle_b.ycor() + 57:
        ball.dx *= -2
        ball.dy /= -ball.dy
        volley_ += 1
        pen.clear()
        pen.write("Player A: {} Player B: {} Volley{}".format(player_a_score, player_b_score, volley_),align="center", font=("Courier", 16, "normal"))
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() < paddle_a.ycor() + 57 and ball.ycor() > paddle_a.ycor() - 57:
        ball.dx *= -2
        # bring back hit angle to 1
        ball.dy /= -ball.dy
        volley_ += 1
        pen.clear()
        pen.write("Player A: {} Player B: {} Volley{}".format(player_a_score, player_b_score, volley_),align="center", font=("Courier", 16, "normal"))
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    # hit with angle? game was a program 
    '''paddle a hit at angle'''
    if ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 57:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    if ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 56:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    if ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 55:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    if ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 54:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    if ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 53:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    if ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 52:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    if ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 52:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    if ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 51:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    if ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 50:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 49:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 48:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 47:
        ball.dy -= 8
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 46:
        ball.dy -= 8
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() - 45:
        ball.dy -= 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))

    if ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() + 51:
        ball.dy += 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() + 50:
        ball.dy += 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416  and ball.ycor() == paddle_a.ycor() + 49:
        ball.dy += 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() + 48:
        ball.dy += 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() + 47:
        ball.dy += 8
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() + 46:
        ball.dy += 8
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() + 45:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() + 44:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() + 43:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() + 42:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == -416 and ball.ycor() == paddle_a.ycor() + 41:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))

    '''paddle b hit at angle'''

    if ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 57:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 56:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 55:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 54:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 53:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 52:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 52:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 51:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 50:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 49:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 48:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 47:
        ball.dy -= 8
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 46:
        ball.dy -= 8
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 45:
        ball.dy -= 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))



    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 44:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 43:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 42:
        ball.dy -= 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 41:
        ball.dy -= 8
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 40:
        ball.dy -= 8
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 39:
        ball.dy -= 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 38:
        ball.dy -= 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 37:
        ball.dy -= 4
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 36:
        ball.dy -= 4
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 35:
        ball.dy -= 4
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 34:
        ball.dy -= 3
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() - 33:
        ball.dy -= 3
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))








    if ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 57:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 56:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 55:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 54:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 53:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 52:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 51:
        ball.dy += 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx,ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 50:
        ball.dy += 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416  and ball.ycor() == paddle_b.ycor() + 49:
        ball.dy += 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 48:
        ball.dy += 10
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 47:
        ball.dy += 8
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 46:
        ball.dy += 8
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 45:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 44:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 43:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 42:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))
    elif ball.xcor() == 416 and ball.ycor() == paddle_b.ycor() + 41:
        ball.dy += 6
        dypen.clear()
        dypen.write("({},{})".format(ball.dx, ball.dy))

    #top paddle b hit at angle

    # ball_wall_bounce
    if ball.ycor() > 380:
        ball.sety(380)
        ball.dy *= -1
    if ball.ycor() < -380:
        ball.sety(-380)
        ball.dy *= -1
    # side_miss_hit
    if ball.xcor() > 450:
        ball.dx /= ball.dx
        ball.dy /= ball.dy
        player_a_score += 1
        volley_ *= 0
        pen.clear()
        pen.write("Player A: {} Player B: {} Volley{}".format(player_a_score, player_b_score, volley_),align="center", font=("Courier", 16, "normal"))
        ball.setpos(0, 0)

    elif ball.xcor() < -450:
        player_b_score += 1
        ball.dx /= ball.dx
        ball.dy /= ball.dy
        volley_ *= 0
        pen.clear()
        pen.write("Player A: {} Player B: {} Volley{}".format(player_a_score, player_b_score, volley_),align="center", font=("Courier", 16, "normal"))
        ball.goto(0, 0)
        volley_ *= 0


