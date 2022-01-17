#!/usr/bin/env python3

import pygame


def main_loop():
    game_notOver = True
    while game_notOver:
        clock.tick(60)

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                game_notOver = False

        redraw()


def redraw():
    window.fill((150, 150, 150))

    for r, row in enumerate(Grid):
        for c, value in enumerate(row):
            pygame.draw.rect(window, (10 * value % 255, 15 * value % 255, 20 * value % 255), (100 * c, 100 * r, 100, 100))
            text = font.render(str(value), True, (0,200,0))
            window.blit(text, (100 * c, 100 * r))



    pygame.display.update()


pygame.display.init()
pygame.font.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 700))

font = pygame.font.SysFont("Verdana", 14)
Grid = [[2, 4, 8, 0], [0, 16, 64, 1], [1024, 32, 0, 4], [0, 16, 8, 1]]

main_loop()

pygame.quit()
