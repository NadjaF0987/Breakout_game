from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        """ Paddles shape, size and color. """
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.max = -350

    def right_move(self):
        """ Moves the paddle to the right. Max ensures that the paddle does not go off the screen. """
        if self.xcor() + 15 > abs(self.max):
            new_x = abs(self.max)
        else:
            new_x = self.xcor() + 15
        self.goto(new_x, self.ycor())

    def left_move(self):
        """ Moves the paddle to the left. max ensures that the paddle does not go off the screen. """
        if self.xcor() - 15 < self.max:
            new_x = self.max
        else:
            new_x = self.xcor() - 15
        self.goto(new_x, self.ycor())

    def paddle_smaller(self):
        """  Decreases the size of the paddle. max is adjusted,
        so paddle can go all the way to the edge, despite the paddle is smaller. """
        self.max = -360
        self.shapesize(stretch_wid=1, stretch_len=4)


