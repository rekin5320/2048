#!/usr/bin/env python3

import pygame


class Text:
    def __init__(self, text, color, font_size):
        self.text_width, self.text_height = font.size(text)
        self.text = font.render(text, True, color)

    def draw(self, x, y):
        window.blit(self.text, (x, y))


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
            x = c * cell_size
            y = r * cell_size
            pygame.draw.rect(window, cell_colors[value], (x, y, cell_size, cell_size))
            if value:
                T = Texts_nums[value]
                T.draw(x + (cell_size - T.text_width) / 2, y + (cell_size - T.text_height) / 2)

    pygame.display.update()


pygame.display.init()
pygame.font.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 700))

font = pygame.font.SysFont("Verdana", 40, bold=True)
Grid = [[2, 4, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 16, 8, 64]]
cell_size = 100

values = [2 ** i for i in range(1, 7 + 1)]

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
Texts_nums = {v: Text(str(v), font_colors[v], 35) for v in values}

main_loop()

pygame.quit()
