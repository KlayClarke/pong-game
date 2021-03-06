from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize()
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x_position = self.xcor() + self.x_move
        new_y_position = self.ycor() + self.y_move
        self.goto(x=new_x_position, y=new_y_position)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.1
        self.bounce_x()


