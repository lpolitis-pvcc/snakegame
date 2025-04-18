import pygame
import random
import sys

# Init
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake and food
snake = [(5, 5)]
direction = (1, 0)
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

def draw_block(pos, color):
    rect = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1): direction = (0, -1)
    if keys[pygame.K_DOWN] and direction != (0, -1): direction = (0, 1)
    if keys[pygame.K_LEFT] and direction != (1, 0): direction = (-1, 0)
    if keys[pygame.K_RIGHT] and direction != (-1, 0): direction = (1, 0)

    # Move snake
    head_x, head_y = snake[0]
    new_head = ((head_x + direction[0]) % GRID_WIDTH, (head_y + direction[1]) % GRID_HEIGHT)

    # Check self collision
    if new_head in snake:
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # Check food
    if new_head == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Draw everything
    screen.fill(BLACK)
    draw_block(food, RED)
    for segment in snake:
        draw_block(segment, GREEN)

    pygame.display.flip()
    clock.tick(10)  # 10 frames per second
