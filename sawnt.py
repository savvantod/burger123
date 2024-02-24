import pygame
import random

pygame.init()

width = 800
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

window = pygame.display.set_mode((width,height))
pygame.display.set_caption ('Змейка')

clock = pygame.time.Clock()

block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 50)

def our_snake(block_size,snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0],x[1],block_size, block_size])

    def message(msg, color):
        msg = font_style.render(msg, True, color)
        window.blit(msg, [width / 6, height / 3])

    def game_loop():
        game_over = False
        game_close = False

        x1 = width / 2
        y1 = height / 2
        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
        foody = round(random.randrange(0, height - block_size) / block_size) * block_size
              
