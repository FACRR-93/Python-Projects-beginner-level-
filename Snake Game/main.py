import time
from turtle import Screen, distance
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600,0,0)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    # update e time são usados para retirar o efeito da animação da cobra (parece uma minhoca sem isto)
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detetar colisao com a comida
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.count()
    #Detetar colisao com paredes
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_on = False
        score.gameover()
    #Detetar colisão com o seu proprio corpo
    for i in snake.segments[1:]:
        if snake.segments[0].distance(i) < 10:
            game_on = False
            score.gameover()

screen.exitonclick()