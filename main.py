from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Bricks

TOTAL_LIVES = 5


def restart_game():
    """ re-sets the game if player writes yes. Else the window closes. """
    question = screen.textinput("GAME OVER", "Do you want to play again? (yes/no)")
    if question == "yes":
        ball.re_set_count = 1
        score.clear_score()
        ball.move_speed = 0.1
        screen.listen()
        return True
    else:
        screen.bye()


# Screen/background
screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor("gray")
screen.title("Breakout")
screen.tracer(0)
# Ball, paddle, bricks, score
ball = Ball((0, -230))
player = Paddle((0, -260))
bricks = Bricks()
score = Scoreboard()
# Screen listen to keypress
screen.listen()
screen.onkey(player.right_move, "Right")
screen.onkey(player.left_move, "Left")

# Game starts. Player has five lives. Player wins in two rounds are finished.
# In the second round speed increase and paddle is smaller.
round_num = 1
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if len(bricks.brick_list) == 0:
        if round_num == 1:
            round_num += 1
            # Continue the game after finalizing the first round.
            bricks = Bricks()
            # Increase speed
            ball.increase_speed()
            # Make paddle smaller
            player.paddle_smaller()
        else:
            # this means that round_count = 2
            if score.score > score.top_score:
                # Update the topscore
                score.save_new_topscore(score.score)
            score.winner()
            # ask if player want to play again.
            if restart_game():
                #bricks.remove_all()
                bricks = Bricks()

    # BALL MOVEMENT
    # ball hits a brick
    for brick in bricks.brick_list:
        if ball.distance(x=brick.xcor()-10, y=brick.ycor()) < 25 or ball.distance(x=brick.xcor()+10, y=brick.ycor()) < 25:
            ball.bounce_y()
            bricks.remove_brick(brick)
            if brick.pencolor() == bricks.color_list[0]:
                score.point(1)
            elif brick.pencolor() == bricks.color_list[1]:
                score.point(3)
            elif brick.pencolor() == bricks.color_list[2]:
                score.point(5)
            elif brick.pencolor() == bricks.color_list[3]:
                score.point(6)
            else:
                score.point(7)

    # ball hits the top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # ball hits right wall or left wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # ball hits the paddle
    if ball.distance(player) < 50 and ball.ycor() <= -240:
        ball.bounce_y()

    # ball passes the paddle and bottom line.
    if ball.ycor() <= -300:
        time.sleep(1)
        ball.re_set()
        score.lost_live()
        if ball.re_set_count > TOTAL_LIVES:
            if score.score > score.top_score:
                # Update the topscore
                score.save_new_topscore(score.score)
            score.game_over()
            # ask if player want to play again.
            if restart_game():
                bricks.remove_all()
                bricks = Bricks()

screen.exitonclick()
