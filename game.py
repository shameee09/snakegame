import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set up colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Set up snake block size
block_size = 20

# Set up clock for controlling snake speed
clock = pygame.time.Clock()

# Set up font for score
font_style = pygame.font.SysFont("bahnschrift", 25)

# Define the snake function
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.circle(screen, GREEN, (x[0] + snake_block // 2, x[1] + snake_block // 2), snake_block // 2)

# Define the food function
def draw_food(x, y):
    pygame.draw.rect(screen, RED, [x, y, block_size, block_size])

# Define the function to display the score
def your_score(score):
    value = font_style.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = width / 2
    y1 = height / 2

    # Initial snake movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, WHITE)
            screen.blit(message, [width / 6, height / 3])
            your_score(Length_of_snake - 1)  # Display the final score
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Handle key events for direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)  # Set background to black
        draw_food(foodx, foody)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(block_size, snake_List)
        your_score(Length_of_snake - 1)  # Display the score

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(8)  # Snake speed

    pygame.quit()
    quit()

gameLoop() 
