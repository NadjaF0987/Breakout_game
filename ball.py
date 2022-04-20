from turtle import Turtle

NORMAL_SPEED = 0.1
FAST_SPEED = 0.5


class Ball(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        """ Visual attributes of the ball and the movement. """
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(start_pos)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = NORMAL_SPEED
        self.re_set_count = 1

    def move(self):
        """ Ball moves according to its current x and y coordinates. """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """ Ball bounces on the y-axis. """
        self.y_move *= -1

    def bounce_x(self):
        """ Ball bounces on the x-axis. """
        self.x_move *= -1

    def increase_speed(self):
        """ Balls speed is increased """
        self.move_speed *= FAST_SPEED

    def re_set(self):
        """ Ball is re-positioned to the center above the paddles line of movement.
        Ball moves upwards with an angle according to the angle it exited the screen with.
        re-set count is increased. """
        self.goto(0, -230)
        self.y_move *= -1
        self.re_set_count += 1
