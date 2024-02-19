from tkinter import *
import random as r

GAME_WIDTH = 500
GAME_HEIGHT = 500

SPEED = 90
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)
            
        
class Food:
    
    def __init__(self):
        
        x = r.randint(0, int(GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = r.randint(0, int(GAME_HEIGHT / SPACE_SIZE) -1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food" )

def next_turn(snake ,food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collection(snake):
        game_over()

    windows.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction



def check_collection(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:

        return True

    elif y < 0 or y >= GAME_HEIGHT:

        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:

            return True

    return False



def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70),text="GAME OVER", fill="red", tags="gameover")

windows = Tk()

windows.title("Snake Game")
windows.resizable(False,False)

score = 0
direction = "down"
label = Label(windows, text="Score:{}".format(score),font=("consolas", 40))
label.pack()

canvas = Canvas(windows, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
windows.update()

window_width = windows.winfo_width()
window_height = windows.winfo_height()
screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

windows.geometry(f"{window_width}x{window_height}+{x}+{y}")

windows.bind('<a>', lambda event: change_direction('left'))
windows.bind('<d>', lambda event: change_direction('right'))
windows.bind('<w>', lambda event: change_direction('up'))
windows.bind('<s>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

windows.mainloop()
