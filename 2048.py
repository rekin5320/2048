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
            self.text = Text(str(value), font_colors[value])

    def draw(self, row, col):
        pygame.draw.rect(window, self.color, (col * cell_size, row * cell_size, cell_size, cell_size))
        if self.value:
            self.text.draw(col * cell_size + (cell_size - self.text.text_width) / 2, row * cell_size + (cell_size - self.text.text_height) / 2)


def move_grid(dir_x, dir_y):
    if dir_x == 1:
        for row in range(0, 4):
            for col1, col2 in zip(range(2, -1, -1), range(3, 0, -1)):
                if not Matrix[row][col2]:  # is empty
                    Matrix[row][col2], Matrix[row][col1], = Matrix[row][col1], Matrix[row][col2]
                elif Matrix[row][col1] == Matrix[row][col2]:  # merge
                    Matrix[row][col2] *= 2
                    Matrix[row][col1] = 0
    elif dir_x == -1:
        for row in range(0, 4):
            for col1, col2 in zip(range(0, 3), range(1, 4)):
                if not Matrix[row][col1]:  # is empty
                    Matrix[row][col2], Matrix[row][col1], = Matrix[row][col1], Matrix[row][col2]
                elif Matrix[row][col1] == Matrix[row][col2]:  # merge
                    Matrix[row][col1] *= 2
                    Matrix[row][col2] = 0
    elif dir_y == 1:
        for col in range(0, 4):
            for row1, row2 in zip(range(2, -1, -1), range(3, 0, -1)):
                if not Matrix[row2][col]:  # is empty
                    Matrix[row1][col], Matrix[row2][col], = Matrix[row2][col], Matrix[row1][col]
                elif Matrix[row1][col] == Matrix[row2][col]:  # merge
                    Matrix[row2][col] *= 2
                    Matrix[row1][col] = 0
    else:  # dir_y == -1
        for col in range(0, 4):
            for row1, row2 in zip(range(0, 3), range(1, 4)):
                if not Matrix[row1][col]:  # is empty
                    Matrix[row1][col], Matrix[row2][col], = Matrix[row2][col], Matrix[row1][col]
                elif Matrix[row1][col] == Matrix[row2][col]:  # merge
                    Matrix[row1][col] *= 2
                    Matrix[row2][col] = 0


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

    for row, row_of_cells in enumerate(Matrix):
        for col, val in enumerate(row_of_cells):
            Cells[val].draw(row, col)

    pygame.display.update()


pygame.display.init()
pygame.font.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((400, 400))

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

Matrix = [[2, 8, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 8, 0, 64]]
Cells = {i: Cell(i) for i in values}


main_loop()

pygame.quit()
