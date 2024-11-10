import tkinter
import random

# Game constants
ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS
game_over = False
score = 0

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

# Adding canvas
canvas = tkinter.Canvas(window, bg='black', width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

# Center window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Initialize game
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
food = Tile(16 * TILE_SIZE, 20 * TILE_SIZE)
velocityX = 0
velocityY = 0
snake_body = []  # List to store body parts

def change_direction(e):
    global velocityX, velocityY, game_over

    if game_over:
        return

    if e.keysym == "Up" and velocityY != 1:
        velocityX = 0
        velocityY = -1
    elif e.keysym == "Down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif e.keysym == "Left" and velocityX != 1:
        velocityX = -1
        velocityY = 0
    elif e.keysym == "Right" and velocityX != -1:
        velocityX = 1
        velocityY = 0

def move():
    global snake, food, snake_body, game_over, score

    if game_over:
        return

    # Check for collision with walls
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True
        return

    # Check for collision with its own body
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            return

    # Check for collision with food
    if snake.x == food.x and snake.y == food.y:
        score += 1
        # Append the current head position to the snake body (this is how the snake "grows")
        snake_body.append(Tile(snake.x, snake.y))
        # Relocate the food to a new random position
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE

    # Move the body by shifting each segment to the position of the previous one
    if len(snake_body) > 0:
        # Insert the current head position into the body list
        snake_body.insert(0, Tile(snake.x, snake.y))
        # Remove the last element to keep the snake length consistent
        snake_body.pop()

    # Move the snake's head
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw():
    global snake, score, game_over

    canvas.delete("all")  # Clear the canvas before redrawing

    move()  # Update the snake's position

    # Draw the snake body
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="blue")

    # Draw the snake's head
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="blue")

    # Draw the food
    canvas.create_oval(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="white")

    # Display score and game over message
    if game_over:
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font="Arial 20", text=f"Game Over: {score}", fill="red")
    else:
        canvas.create_text(30, 20, font="Arial 12", text=f"Score: {score}", fill='white')

    window.after(100, draw)  # Call draw() again after 100ms

# Start drawing
draw()

# Bind keypress to control direction
window.bind("<KeyRelease>", change_direction)
window.mainloop()
