import pygame
import random

square_size: int = 10
enemy_size = random.randrange(0,20)
dot_size1 = 10
dot_size2 = 10
dot_size3 = 10
window_size = (1300, 700)
color = (235, 226, 213)
red = 235, 0, 0
blue = 0, 235, 0
green = 0, 0, 235
black = (0, 0, 0)
lead_x = window_size[0] / 2
lead_y = window_size[1] / 2
pace_x = 0
pace_y = 0
step_pace = 5
speed = [2, 2]
# ====================

pygame.init()

game_display = pygame.display.set_mode(window_size)
game_display.fill(color)
pygame.draw.rect(game_display, black, [lead_x, lead_y, square_size, square_size])
random_dot_x1 = random.randrange(0, 1300 - 10)
random_dot_y1 = random.randrange(0, 700 - 10)
random_dot_x2 = random.randrange(0, 1300 - 10)
random_dot_y2 = random.randrange(0, 700 - 10)
random_dot_x3 = random.randrange(0, 1300 - 10)
random_dot_y3 = random.randrange(0, 700 - 10)
random_dot_x4 = random.randrange(0, 1300 - 10)
random_dot_y4 = random.randrange(0, 700 - 10)
pygame.draw.rect(game_display, blue, [random_dot_x4, random_dot_y4, enemy_size, enemy_size])
pygame.draw.rect(game_display, red, [random_dot_x1, random_dot_y1, dot_size1, dot_size1])
pygame.draw.rect(game_display, blue, [random_dot_x2, random_dot_y2, dot_size2, dot_size2])
pygame.draw.rect(game_display, green, [random_dot_x3, random_dot_y3, dot_size3, dot_size3])
pygame.display.update()
# ====================
game_exit = False
while not game_exit:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                pace_x = - step_pace
                pace_y = 0

            if event.key == pygame.K_RIGHT:
                pace_x = step_pace
                pace_y = 0

            if event.key == pygame.K_UP:
                pace_y = - step_pace
                pace_x = 0

            if event.key == pygame.K_DOWN:
                pace_y = step_pace
                pace_x = 0
    if (random_dot_x1 <= lead_x <= random_dot_x1 + dot_size1 or random_dot_x1 <= lead_x + dot_size1 <= random_dot_x1 + dot_size1) and (
            random_dot_y1 <= lead_y <=  random_dot_y1 + dot_size1 or random_dot_y1 <= lead_y + dot_size1 <= random_dot_y1 + dot_size1):
        square_size += 2
        dot_size1 = 0

    if (random_dot_x2 <= lead_x <= random_dot_x2 + dot_size2 or random_dot_x2 <= lead_x + dot_size2 <= random_dot_x2 + dot_size2) and (
            random_dot_y2 <= lead_y <=  random_dot_y2 + dot_size2 or random_dot_y2 <= lead_y + dot_size2 <= random_dot_y2 + dot_size2):
        square_size += 2
        dot_size2 = 0

    if (random_dot_x3 <= lead_x <= random_dot_x3 + dot_size3 or random_dot_x3 <= lead_x + dot_size3 <= random_dot_x3 + dot_size3) and (
            random_dot_y3 <= lead_y <=  random_dot_y3 + dot_size3 or random_dot_y3 <= lead_y + dot_size3 <= random_dot_y3 + dot_size3):
        square_size += 2
        dot_size3 = 0

    lead_x += pace_x
    lead_y += pace_y
    game_display.fill(color)
    pygame.draw.rect(game_display, black, [lead_x, lead_y, square_size, square_size])
    pygame.draw.rect(game_display, red, [random_dot_x1, random_dot_y1, dot_size1, dot_size1])
    pygame.draw.rect(game_display, blue, [random_dot_x2, random_dot_y2, dot_size2, dot_size2])
    pygame.draw.rect(game_display, green, [random_dot_x3, random_dot_y3, dot_size3, dot_size3])
    pygame.display.update()

# ====================

pygame.quit()
quit()