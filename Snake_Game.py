import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize game variables
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
direction = RIGHT
score = 0
snake_speed = 13
snake_speed_change = 0.0

# Font for the score counter
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            if event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            if event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            if event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    # Move the snake
    x, y = snake[0]
    new_head = (x + direction[0], y + direction[1])
    snake.insert(0, new_head)

    # Check for collisions
    if snake[0] == food:
        score += 1
        snake_speed_change += 0.2

        # Check if snake_speed_change is 1 or more, and reset it to 0
        if snake_speed_change >= 1.2:
            snake_speed_change = 0

        snake_speed = round(snake_speed + snake_speed_change)
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
        or snake[0] in snake[1:]
    ):
        running = False

    # Draw everything
    window.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(window, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(window, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Render and display the score
    text = font.render(f"Score: {score}", True, GREEN)
    window.blit(text, (10, 10))

    pygame.display.update()

    pygame.time.delay(1000 // snake_speed)

pygame.quit()

# Write Scores to File and Screen
MyFile = open("Snake_Game_Scores.txt", "a")
MyFile.write(str(score) + "\n")
MyFile.close()
print("Game Over! Your score was: ", score)