import random

import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 700
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize clock
clock = pygame.time.Clock()

# Initialize snake
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_dir = (1, 0)  # Initial direction (right)

# Initialize apple
apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Initialize game variables
score = 0
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, 1):
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -1):
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT and snake_dir != (1, 0):
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-1, 0):
                snake_dir = (1, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Check for collisions
    if snake[0] == apple:
        score += 1
        apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
        or snake[0] in snake[1:]
    ):
        game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw apple
    pygame.draw.rect(screen, RED, (apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Update display
    pygame.display.update()

    # Control game speed
    clock.tick(10)

# Game over message
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over", True, (255, 0, 0))
score_text = font.render(f"Score: {score}", True, (0, 0, 0))
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
screen.blit(score_text, (WIDTH // 2 - 50, HEIGHT // 2 + 10))
pygame.display.update()

# Wait for a few seconds before closing
pygame.time.delay(2000)

# Quit Pygame
pygame.quit()
pygame.quit()
