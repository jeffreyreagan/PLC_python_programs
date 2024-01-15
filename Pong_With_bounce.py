
import turtle

wn = turtle.Screen()
wn.setup(width=1000,height=800)
wn.tracer()
wn.bgcolor("white")
#game loop

#score
player_a_score = 0
player_b_score = 0

#volley
volley_ = 0

#objects

#paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-450,0)
paddle_a.color("red")

#paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("pink")
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(450,0)

#ball

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(1.25)
ball.goto(0,0)
ball.dx = 2
ball.dy = 1
ball.fx= 1
ball.penup()
ball.speed(0)

#pen

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed()
pen.setpos(0,300)
pen.write("Player A:0 Player B:0 Volley:0")



#functions

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

#keybindings

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#game_loop
while True:
    wn.update()

    # ball_movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # hit!
    if ball.xcor() > 425 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        ball.dx *= 2
        ball.dy /= ball.dy
        volley_ += 1
        pen.clear()
        pen.write("Player A: {} Player B: {} Volley{}".format(player_a_score, player_b_score, volley_))

    elif ball.xcor() < -425 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        ball.dx *= 2
        #bring back hit angle to 1
        ball.dy /= ball.dy
        volley_ += 1
        pen.clear()
        pen.write("Player A: {} Player B: {} Volley{}".format(player_a_score, player_b_score, volley_))

    # hit with angle? game was a program
    if ball.xcor() > 425 and ball.ycor() == (paddle_b.ycor() - 50) or (paddle_b.ycor() - 49) or (paddle_b.ycor() - 48) or (paddle_b.ycor() -46) or (paddle_b.ycor() - 45) or (paddle_b.ycor() - 44) or (paddle_b.ycor() - 43):
        ball.dy -= 4


#ball_wall_bounce
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1
    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1
  #side_miss_hit
    if ball.xcor() > 490:
        ball.dx *= -1
        player_a_score += 1
        volley_ *= 0
        pen.clear()
        pen.write("Player A: {} Player B: {} Volley{}".format(player_a_score, player_b_score, volley_))
        ball.setpos(0, 0)
        ball.dx = 1
    elif ball.xcor() < -490:
        player_b_score += 1
        ball.dx *= -1
        volley_ *= 0
        pen.clear()
        pen.write("Player A: {} Player B: {} Volley{}".format(player_a_score, player_b_score, volley_))
        ball.goto(0, 0)
        ball.dx = 1
        volley_ *= 0
    if ball.dx >= 32:
        ball.dx = 16
