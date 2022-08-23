#
#
#
import pygame
from pygame import Color


def init_screen(caption):
    black = (0,0,0)
    (width, height) = (800, 800)

    screen = pygame.display.set_mode((width, height), depth=32)
    pygame.display.set_caption(caption)
    screen.fill(black)
    return screen


def main():
    white = (255, 255, 255)
    red = Color(255, 0, 0)
    dim_red1 = Color(200, 0, 0)
    dim_red2 = Color(150, 0, 0)
    screen = init_screen('Key Draw')
    width = screen.get_width()
    height = screen.get_height()
    start_pos = (width / 2, height / 2)
    cur_pos = start_pos
    new_pos = start_pos
    draw = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("quit.")
            if event.type == pygame.TEXTINPUT and event.text == 'w':
                new_pos = (cur_pos[0], cur_pos[1] - 5)
                draw = True
            if event.type == pygame.TEXTINPUT and event.text == 'a':
                new_pos = (cur_pos[0] - 5, cur_pos[1])
                draw = True
            if event.type == pygame.TEXTINPUT and event.text == 's':
                new_pos = (cur_pos[0], cur_pos[1] + 5)
                draw = True
            if event.type == pygame.TEXTINPUT and event.text == 'd':
                new_pos = (cur_pos[0] + 5, cur_pos[1])
                draw = True
            if event.type == pygame.KEYDOWN and event.unicode == 'q':
                print('Quit.')
                running = False
        if draw:
            pygame.draw.line(screen, dim_red2, cur_pos, new_pos, width=9)
            pygame.draw.line(screen, dim_red1, cur_pos, new_pos, width=5)
            pygame.draw.line(screen, red, cur_pos, new_pos, width=3)

            pygame.display.flip()
            cur_pos = new_pos

    pygame.quit()

if __name__ == '__main__':
    main()
