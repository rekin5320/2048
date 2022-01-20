#!/usr/bin/env python3

import pygame


class Text:
    def __init__(self, text, color):
        self.text_width, self.text_height = font.size(text)
        self.text = font.render(text, True, color)

    def draw(self, x, y):
        window.blit(self.text, (x, y))


class Cell:
    def __init__(self, value):
        self.value = value
        self.color = cell_colors[value]
        if value:
            self.text = Texts_nums[value]

    def draw(self, row, col):
        pygame.draw.rect(window, self.color, (col * cell_size, row * cell_size, cell_size, cell_size))
        if self.value:
            self.text.draw(col * cell_size + (cell_size - self.text.text_width) / 2, row * cell_size + (cell_size - self.text.text_height) / 2)


def move_grid(dir_x, dir_y):
    global Grid
    if dir_x == 1:
        for yy in range(0, 4):
            for xx1, xx2 in zip(range(0, 3), range(1, 4)):
                if not Grid[xx2][yy]:  # is empty
                    Grid[xx1][yy], Grid[xx2][yy], = Grid[xx2][yy], Grid[xx1][yy]
    elif dir_x == -1:
        pass
    else:
        for c in range(4):
            for yy in (range(0, 5, 1) if dir_y == 1 else range(5, 0, -1)):
                print(yy, c)


def main_loop():
    game_notOver = True
    moved = False
    dir_x, dir_y = 0, 0
    while game_notOver:
        clock.tick(60)

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                game_notOver = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            moved = True
            dir_x = -1
            dir_y = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            moved = True
            dir_x = 1
            dir_y = 0
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            moved = True
            dir_x = 0
            dir_y = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            moved = True
            dir_x = 0
            dir_y = 1

        if moved:
            move_grid(dir_x, dir_y)
        moved = False

        redraw()


def redraw():
    window.fill((250, 248, 239))

    for c, row in enumerate(Grid):
        for r, val in enumerate(row):
            Cells[val].draw(r, c)

    pygame.display.update()


pygame.display.init()
pygame.font.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 700))

font = pygame.font.SysFont("Verdana", 40, bold=True)

cell_size = 100

values = [0] + [2 ** i for i in range(1, 7 + 1)]

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
Texts_nums = {v: Text(str(v), font_colors[v]) for v in values[1:]}

Grid = [[2, 4, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 16, 8, 64]]
Cells = {i: Cell(i) for i in values}


main_loop()

pygame.quit()
