#
#
#
import math

import pygame
from pygame import Color
import time


def init_screen(caption):
    black = (0, 0, 0)
    (width, height) = (800, 800)

    screen = pygame.display.set_mode((width, height), depth=32)
    pygame.display.set_caption(caption)
    screen.fill(black)
    return screen


def draw_it(screen, cur_pos, new_pos):
    red = Color(255, 0, 0)
    dim_red1 = Color(200, 0, 0)
    dim_red2 = Color(150, 0, 0)
    pygame.draw.line(screen, dim_red2, cur_pos, new_pos, width=9)
    pygame.draw.line(screen, dim_red1, cur_pos, new_pos, width=5)
    pygame.draw.line(screen, red, cur_pos, new_pos, width=3)

    pygame.display.flip()


def main():
    black = (0, 0, 0, 255)
    screen = init_screen('Key Draw')
    width = screen.get_width()
    height = screen.get_height()
    start_pos = (math.ceil(width / 2), math.ceil(height / 2))
    cur_pos = start_pos
    new_pos = start_pos
    draw = False
    running = True
    direction = ""
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("quit.")
            if event.type == pygame.TEXTINPUT and event.text == 'w':
                direction = "north"
                draw = True
            if event.type == pygame.TEXTINPUT and event.text == 'a':
                direction = "west"
                draw = True
            if event.type == pygame.TEXTINPUT and event.text == 's':
                direction = "south"
                draw = True
            if event.type == pygame.TEXTINPUT and event.text == 'd':
                direction = "east"
                draw = True
            if event.type == pygame.TEXTINPUT and event.text == ' ':
                draw = False
            if event.type == pygame.KEYDOWN and event.unicode == 'q':
                print('Quit.')
                running = False

        if direction == "north" and draw:
            new_pos = (cur_pos[0], cur_pos[1] - 5)
            if screen.get_at(new_pos) != black:
                print("*****BOOM*****")
            draw_it(screen, cur_pos, new_pos)
            cur_pos = new_pos
        if direction == "west" and draw:
            new_pos = (cur_pos[0] - 5, cur_pos[1])
            if screen.get_at(new_pos) != black:
                print("*****BOOM*****")
            draw_it(screen, cur_pos, new_pos)
            cur_pos = new_pos
        if direction == "south" and draw:
            new_pos = (cur_pos[0], cur_pos[1] + 5)
            if screen.get_at(new_pos) != black:
                print("*****BOOM*****")
            draw_it(screen, cur_pos, new_pos)
            cur_pos = new_pos
        if direction == "east" and draw:
            new_pos = (cur_pos[0] + 5, cur_pos[1])
            if screen.get_at(new_pos) != black:
                print("*****BOOM*****")
            draw_it(screen, cur_pos, new_pos)
            cur_pos = new_pos
        time.sleep(0.01)

    pygame.quit()


if __name__ == '__main__':
    main()
