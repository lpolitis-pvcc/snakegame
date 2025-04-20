import pygame
import random
import sys

# Setup
pygame.init()

CELL_SIZE = 50  # has to be at least 10x10
GRID_SIZE = 20
WIDTH = HEIGHT = CELL_SIZE * GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Leo's Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 75, 0)

# Snake
snake = [(5, 5)]
direction = (0, 0)  # stationary
food = (random.randint(0, 9), random.randint(0, 9))
score = 0
game_over = False

# Functions
def draw_block(pos, color):
    rect = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

def show_game_over():
    text = font.render(f"Game Over! Score: {score}", True, WHITE)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))  # vertical lines
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))   # horizontal lines

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # Handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, 1): direction = (0, -1)
        if keys[pygame.K_DOWN] and direction != (0, -1): direction = (0, 1)
        if keys[pygame.K_LEFT] and direction != (1, 0): direction = (-1, 0)
        if keys[pygame.K_RIGHT] and direction != (-1, 0): direction = (1, 0)
        if keys[pygame.K_w] and direction != (0, 1): direction = (0, -1)
        if keys[pygame.K_s] and direction != (0,-1): direction = (0, 1)
        if keys[pygame.K_a] and direction != (1, 0): direction = (-1, 0)
        if keys[pygame.K_d] and direction != (-1, 0): direction = (1, 0)

        if direction != (0, 0):  # Snake has started moving
            # Move snake
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            # Check wall collision
            if not (0 <= new_head[0] < GRID_SIZE) or not (0 <= new_head[1] < GRID_SIZE):
                game_over = True

            # Check self collision
            elif new_head in snake:
                game_over = True

            else:
                snake.insert(0, new_head)

                # Check food
                if new_head == food:
                    score += 1
                    while food in snake:
                        food = (random.randint(0, 9), random.randint(0, 9))
                else:
                    snake.pop()

    # Draw
    screen.fill(BLACK)

    for segment in snake:
        draw_block(segment, GREEN)

    draw_block(food, RED)

    if game_over:
        show_game_over()

    pygame.display.flip()
    clock.tick(9)  # Control the speed
