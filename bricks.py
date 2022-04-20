from turtle import Turtle

# rgb color numbers
COL_1 = (235, 101, 91)
COL_2 = (221, 235, 91)
COL_3 = (101, 194, 113)
COL_4 = (102, 199, 204)
COL_5 = (103, 113, 201)


class Bricks:
    def __init__(self):
        """ Start position for the first item/brick. Creates all the items/bricks with the
        make_brick function according to the color list """
        self.x_pos = -365
        self.y_pos = 50
        self.brick_list = []
        self.color_list = [COL_1, COL_2, COL_3, COL_4, COL_5]
        self.make_brick()

    def make_brick(self):
        """ Creates square shaped items n rows as n items in color_list. Each row of items has the same unique color.
        Appends all the bricks/items to a list. """
        for color in self.color_list:
            for _ in range(17):
                new_brick = Turtle("square")
                new_brick.penup()
                new_brick.shapesize(stretch_wid=1, stretch_len=2)
                new_brick.goto(self.x_pos, self.y_pos)
                new_brick.color(color)
                self.brick_list.append(new_brick)
                self.x_pos += 45
            self.x_pos = self.x_pos - 765
            self.y_pos = self.y_pos + 30

    def remove_brick(self, item):
        """ Deletes the item/brick that is passed as input.
        The brick is both removed from the brick list and the screen. """
        self.brick_list.remove(item)
        item.clear()
        item.hideturtle()

    def remove_all(self):
        """ Deletes all bricks/items in the brick list and removes them from the screen """
        for item in self.brick_list:
            item.reset()
            item.hideturtle()
