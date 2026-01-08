from turtle import Turtle
# posicoes inicais dos segmentos da cobra
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):

        # lista que vai conter cada segmento e que vai ser usada para controlar todos os mesmos para mudar de direção
        self.segments = []
        self.create_snake()

        # criar 3 segmentos iniciais da cobra (3 porque so escolhemos 3 starting positions)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # para controlar os segmentos e evitar que a cabeça da cobra seja a unica coisa a mudar de direção
        # len(segments) = 3 e como a lista vai de 0 a 2, temos de subtrair por 1
        # range(start, stop, step)
        # (começo, fim, de quanto em quanto)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # new_x e new_y vão ser as novas posições de todos os segmentos que não sejam o primeiro
            # 3 segmentos: o segundo e o terceiro vão se mover para a posição do segmento anterior; o primeiro segmento é que vai "controlar" o resto
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)



