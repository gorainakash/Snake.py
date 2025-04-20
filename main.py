from turtle import Turtle , Screen
import time
import random
from snake import Snake
from food import Food
from score import Score
from special import SpecialFood
SPEED = 0.1
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("🐍🐍Phisssss-Phissssss🐍🐍")
game_is_on = True
snake = Snake()
food = Food()
screen.listen()
score = Score()
screen.onkey(snake.up, "Up",)
screen.onkey(snake.down, "Down" )
screen.onkey(snake.right, "Right" )
screen.onkey(snake.left, "Left")
border = Turtle()
border.hideturtle()
border.color("white")
border.penup()
border.goto(-295, 295)  # Top-left corner
border.pendown()
border.pensize(5)

for _ in range(4):
    border.forward(585)
    border.right(90)
special_food = SpecialFood()
special_food_timer = 0
SPECIAL_FOOD_DURATION = 50
SPECIAL_FOOD_INTERVAL = 200

while game_is_on:
    screen.update()
    time.sleep(SPEED)

    snake.move()

    if snake.head.distance(food) < 14:
        SPEED *= 0.98
        food.refresh()
        score.inc()
        snake.extend_s()

    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280 :
        game_is_on = False
        score.game_o()

    for z in snake.segment[1:]:
        if snake.head.distance(z) <10:
            game_is_on = False
            score.game_o()

    if special_food.active:
        special_food_timer += 1
        if special_food_timer > SPECIAL_FOOD_DURATION:
            special_food.despawn()
            special_food_timer = 0
    else:
        if random.randint(1, SPECIAL_FOOD_INTERVAL) == 1:
            special_food.spawn()

    if special_food.active and snake.head.distance(special_food) < 14:
        effect = special_food.type
        special_food.despawn()
        special_food_timer = 0

        if effect == "score":
            score.score += 3
        elif effect == "slow":
            SPEED *= 0.8
        elif effect == "poison":
            SPEED *= 1.15
        score.clear()
        score.up()














screen.exitonclick()
