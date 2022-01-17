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
    window.fill((250, 248, 239))

    for r, row in enumerate(Grid):
        for c, value in enumerate(row):
            pygame.draw.rect(window, cell_colors[value], (100 * c, 100 * r, 100, 100))
            if value:
                text = font.render(str(value), True, font_colors[value])
                window.blit(text, (100 * c, 100 * r))

    pygame.display.update()


pygame.display.init()
pygame.font.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 700))

font = pygame.font.SysFont("Verdana", 35)
Grid = [[2, 4, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 16, 8, 64]]

cell_colors = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
}

font_colors = {
    2: (119, 110, 98),
    4: (119, 110, 98),
    8: (249, 246, 242),
    16: (249, 246, 242),
    32: (249, 246, 242),
    64: (249, 246, 242),
    128: (249, 246, 242),
}

main_loop()

pygame.quit()
