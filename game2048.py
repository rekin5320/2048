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


def merge_cells(row_absorbent, col_absorbent, row_absorbed, col_absorbed):
    Matrix[row_absorbent][col_absorbent] *= 2
    Matrix[row_absorbed][col_absorbed] = 0


def find_maximum_movement(row_start, col_start, dir_x, dir_y):
    if dir_x != 0:  # x direction
        col_end = col_start + dir_x
        while 0 < col_end < 3 and not Matrix[row_start][col_end] and ((not Matrix[row_start][col_end + dir_x]) or Matrix[row_start][col_start] == Matrix[row_start][col_end + dir_x]):
            col_end += dir_x
        return col_end
    else:  # y direction
        row_end = row_start + dir_y
        while 0 < row_end < 3 and not Matrix[row_end][col_start] and ((not Matrix[row_end + dir_y][col_start]) or Matrix[row_start][col_start] == Matrix[row_end + dir_y][col_start]):
            row_end += dir_y
        return row_end


def move_cells(dir_x, dir_y):
    if dir_x != 0:  # x direction
        for row in range(0, 4):
            for col_start in (range(2, -1, -1) if dir_x > 0 else range(0, 4)):
                if not ((col_start == 0 and dir_x < 0) or (col_start == 3 and dir_x > 0)):
                    col_end = find_maximum_movement(row, col_start, dir_x, dir_y)
                    if col_start != col_end:
                        if not Matrix[row][col_end]:  # is empty
                            Matrix[row][col_end] = Matrix[row][col_start]
                            Matrix[row][col_start] = 0
                        elif Matrix[row][col_start] == Matrix[row][col_end]:
                            merge_cells(row, col_end, row, col_start)
    else:  # y direction
        for col in range(0, 4):
            for row_start in (range(2, -1, -1) if dir_y > 0 else range(0, 4)):
                if not ((row_start == 0 and dir_y < 0) or (row_start == 3 and dir_y > 0)):
                    row_end = find_maximum_movement(row_start, col, dir_x, dir_y)
                    if row_start != row_end:
                        if not Matrix[row_end][col]:  # is empty
                            Matrix[row_end][col] = Matrix[row_start][col]
                            Matrix[row_start][col] = 0
                        elif Matrix[row_start][col] == Matrix[row_end][col]:
                            merge_cells(row_end, col, row_start, col)


def main_loop():
    game_notOver = True
    move_time_remaining = 0
    dir_x, dir_y = 0, 0
    while game_notOver:
        clock.tick(fps)

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                game_notOver = False

        if not move_time_remaining:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                move_time_remaining = move_time
                dir_x = -1
                dir_y = 0
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                move_time_remaining = move_time
                dir_x = 1
                dir_y = 0
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                move_time_remaining = move_time
                dir_x = 0
                dir_y = -1
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                move_time_remaining = move_time
                dir_x = 0
                dir_y = 1

            if move_time_remaining:
                move_cells(dir_x, dir_y)
        else:
            move_time_remaining -= 1

        redraw()


def redraw():
    window.fill((250, 248, 239))

    for row, row_of_cells in enumerate(Matrix):
        for col, val in enumerate(row_of_cells):
            Cells[val].draw(row, col)

    pygame.display.update()


cell_size = 100
fps = 60
move_time = fps * 1

values = [0] + [2 ** i for i in range(1, 10 + 1)]

cell_colors = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (238, 225, 201),
    8: (243, 178, 122),
    16: (246, 150, 100),
    32: (247, 124, 95),
    64: (247, 95, 59),
    128: (237, 208, 115),
    256: (237, 204, 98),
    512: (237, 201, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

font_colors = {
    2: (119, 110, 101),
    4: (119, 110, 101),
    8: (249, 246, 242),
    16: (249, 246, 242),
    32: (249, 246, 242),
    64: (249, 246, 242),
    128: (249, 246, 242),
    256: (249, 246, 242),
    512: (249, 246, 242),
    1024: (249, 246, 242),
    2048: (249, 246, 242),
}

Matrix = [[2, 8, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 8, 0, 64]]


if __name__ == "__main__":
    pygame.display.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((400, 400))

    font = pygame.font.SysFont("Verdana", 40, bold=True)
    Cells = {i: Cell(i) for i in values}

    main_loop()

    pygame.quit()
