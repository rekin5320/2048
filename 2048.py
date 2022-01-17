#!/usr/bin/env python3

import pygame


class Text:
    def __init__(self, text, color, font_size):
        self.text_width, self.text_height = font.size(text)
        self.text = font.render(text, True, color)

    def draw(self, x, y):
        window.blit(self.text, (x, y))


class Cell:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.color = cell_colors[value]
        if value:
            self.text = Texts_nums[value]

    def draw(self):
        pygame.draw.rect(window, self.color, (self.x * cell_size, self.y * cell_size, cell_size, cell_size))
        if self.value:
            self.text.draw(self.x * cell_size + (cell_size - self.text.text_width) / 2, self.y * cell_size + (cell_size - self.text.text_height) / 2)


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

    for row in Grid:
        for cell in row:
            cell.draw()

    pygame.display.update()


pygame.display.init()
pygame.font.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 700))

font = pygame.font.SysFont("Verdana", 40, bold=True)

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

Grid = [[2, 4, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 16, 8, 64]]
for r in range(4):
    for c in range(4):
        Grid[r][c] = Cell(Grid[r][c], r, c)

main_loop()

pygame.quit()
