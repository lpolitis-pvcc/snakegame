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
snake = [(9, 9)]
direction = (0, 0)
food = (random.randint(0, 19), random.randint(0, 19))
score = 0
game_over = False

# Functions
def draw_block(pos, color, radius=1):
    rect = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect, border_radius=radius)

def show_game_over():
    text1 = font.render(f"Game Over! Score: {score}", True, WHITE)
    text2 = font.render(f"Press R or Space to Restart", True, WHITE)
    screen.blit(text1, (WIDTH//2 - text1.get_width()//2, HEIGHT//2 - text1.get_height()//2))
    screen.blit(text2, (WIDTH//2 - text2.get_width()//2, HEIGHT//2 + 10))

def draw_score(surface):
    text = font.render(f"Score: {score}", True, (WHITE))
    surface.blit(text, (10,10))

def draw_background():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            color = DARK_GREEN if (x+y) % 2 == 0 else (0, 60, 0)
            draw_block((x, y), color)

# Game Loop
while True:
    # input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
                    direction = (0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
                    direction = (0, 1)
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                    direction = (1, 0)
            else:
                # restart game by pressing r or space
                if event.key == pygame.K_r:
                    snake = [(9, 9)]
                    direction = (0, 0)
                    food = (random.randint(0, 19), random.randint(0, 19))
                    score = 0
                    game_over = False
                elif event.key == pygame.K_SPACE:
                    snake = [(9, 9)]
                    direction = (0, 0)
                    food = (random.randint(0, 19), random.randint(0, 19))
                    score = 0
                    game_over = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and direction != (0, 1):
            direction = (0, -1)
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and direction != (0, -1):
            direction = (0, 1)
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and direction != (1, 0):
            direction = (-1, 0)
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and direction != (-1, 0):
            direction = (1, 0)

        if direction != (0, 0):  # Snake is moving
            # Move snake
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            # Check wall collision
            if not (0 <= new_head[0] < GRID_SIZE) or not (0 <= new_head[1] < GRID_SIZE):
                game_over = True
            # Check snake collision
            elif new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)

                # Check food
                if new_head == food:
                    score += 1
                    while food in snake:
                        food = (random.randint(0, 19), random.randint(0, 19))
                else:
                    snake.pop()

    # Draw
    screen.fill(BLACK)
    draw_background()
    for segment in snake:
        draw_block(segment, GREEN, radius=3)

    draw_block(food, RED, radius=20)
    draw_score(screen)

    if game_over:
        show_game_over()

    pygame.display.flip()
    clock.tick(11)

