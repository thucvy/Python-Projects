import turtle as t

STARTING_POSITIONS = [(0,0),(-10,0),(-20,0)]
STEP = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    # TODO: Create a snake body (3 squares on the screen)
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.end = self.snake_body[-1]


    def add_body(self, position):
        snake_part = t.Turtle()
        snake_part.color("white")
        snake_part.shape("square")
        snake_part.pu()
        snake_part.goto(position)
        self.snake_body.append(snake_part)


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)


    def extend_snake(self):
        for _ in range (3):
            position = self.end.position()
            self.add_body(position)

    def reset(self):
        for snake_part in self.snake_body:
            snake_part.goto((1000,1000))
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
        self.end = self.snake_body[-1]

    # TODO: Move the snake
    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].position())
        self.head.fd(STEP)

    def right_key(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up_key(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down_key(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left_key(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)




