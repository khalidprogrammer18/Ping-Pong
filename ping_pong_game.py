import turtle

wind = turtle.Screen()

wind.title("ping pong game")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_wid=5,stretch_len=1)
player1.color("blue")
player1.penup()
player1.goto(-350,0)

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_wid=5,stretch_len=1)
player2.color("red")
player2.penup()
player2.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

# Initialize difficulty variables
Hard = False
Medium = False
Easy = True  # Default to Easy

def set_hard():
    global Hard, Medium, Easy
    Hard = True
    Medium = False
    Easy = False
    set_ball_speed()

def set_medium():
    global Hard, Medium, Easy
    Hard = False
    Medium = True
    Easy = False
    set_ball_speed()

def set_easy():
    global Hard, Medium, Easy
    Hard = False
    Medium = False
    Easy = True
    set_ball_speed()

def set_ball_speed():
    if Hard:
        ball.dx = 0.75
        ball.dy = -0.75
    elif Medium:
        ball.dx = 0.5
        ball.dy = -0.5
    else:
        ball.dx = 0.25
        ball.dy = -0.25

set_ball_speed()

wind.listen()
wind.onkeypress(set_hard, "h")
wind.onkeypress(set_medium, "m")
wind.onkeypress(set_easy, "e")

score1=0
score2=0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,270)


def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)
    if y > 220:
        y = 220
        player1.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)
    if y < -220:
        y = -220
        player1.sety(y)

def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)
    if y > 220:
        y = 220
        player2.sety(y)


def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)
    if y < -220:
        y = -220
        player2.sety(y)

wind.listen()
wind.onkeypress(player1_up,"w")
wind.onkeypress(player1_down,"s")
wind.onkeypress(player2_up,"Up")
wind.onkeypress(player2_down,"Down")

while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor() + ball.dy )

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right wall
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        ball.dx = 0.25
        ball.dy = 0.25

    # Left wall
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        ball.dx = 0.25
        ball.dy = 0.25

    # Paddle collision
    if (340 < ball.xcor() < 350) and (player2.ycor() - 50 < ball.ycor() < player2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (player1.ycor() - 50 < ball.ycor() < player1.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    # Update the score display
    score.clear()
    score.write(f"player 1: {score1}    player2: {score2}", align="center", font=("courier", 20, "normal"))