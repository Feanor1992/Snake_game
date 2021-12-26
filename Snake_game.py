import time
import random
import pygame

pygame.init()

game_display_width = 800
game_display_height = 600
game_display = pygame.display.set_mode((game_display_width, game_display_height))

pygame.display.set_caption('Snake game by Artem L on PyGame.       ver 1.0.1')
font = pygame.font.SysFont('times new roman', 25)
score_font = pygame.font.SysFont('comicsansms', 20)

timer = pygame.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)
green = (48, 186, 143)
black = (0, 0, 0)
yellow = (252, 221, 118)
blue = (65,105,225)

snake_block = 10
snake_speed = 20


def snake(snake_blocks, snake_lists):
    for coordinate in snake_lists:
        pygame.draw.rect(game_display, white, [coordinate[0], coordinate[1], snake_blocks, snake_blocks])


def text(message, color):
    message_text = font.render(message, True, color)
    game_display.blit(message_text, [game_display_width / 6, game_display_height / 3])


def score(scores):
    your_score = score_font.render('Your score: ' + str(scores), True, blue)
    game_display.blit(your_score, [0, 0])


def game():
    game_over = False
    game_close = False

    x = game_display_width / 2
    y = game_display_height / 2
    x_change = 0
    y_change = 0

    snake_list = list()
    snake_len = 1

    food_x = round(random.randrange(0, game_display_width - snake_block) / 10) * 10
    food_y = round(random.randrange(0, game_display_height - snake_block) / 10) * 10

    while not game_over:
        while game_close == True:
            text('You Lose! Press "c" to play again, "q" if you wanna quit', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block

        if (x >= game_display_width) or (y >= game_display_height) or (x < 0) or (y < 0):
            game_close = True

        x += x_change
        y += y_change

        game_display.fill(green)

        pygame.draw.rect(game_display, yellow, [food_x, food_y, snake_block, snake_block])
        pygame.display.update()

        snake_head = list()
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_len:
            del snake_list[0]

        for elem in snake_list[:-1]:
            if elem == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        score(snake_len - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, game_display_width - snake_block) / 10) * 10
            food_y = round(random.randrange(0, game_display_height - snake_block) / 10) * 10
            snake_len += 1

        timer.tick(snake_speed)

    pygame.quit()
    quit()


game()
