"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
import turtle
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        turtle.update()  # Using explicit turtle reference
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    turtle.clear()  # Using explicit turtle reference

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    turtle.update()  # Using explicit turtle reference
    turtle.ontimer(move, 100)  # Using explicit turtle reference


turtle.setup(420, 420, 370, 0)  # Using explicit turtle reference
turtle.hideturtle()  # Using explicit turtle reference
turtle.tracer(False)  # Using explicit turtle reference
turtle.listen()  # Using explicit turtle reference
turtle.onkey(lambda: change(10, 0), 'Right')
turtle.onkey(lambda: change(-10, 0), 'Left')
turtle.onkey(lambda: change(0, 10), 'Up')
turtle.onkey(lambda: change(0, -10), 'Down')
move()
turtle.done()  # Using explicit turtle reference
