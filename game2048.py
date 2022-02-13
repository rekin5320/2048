#!/usr/bin/env python3

import pygame
import random


class Colors:
    background = (250, 248, 239)
    board_background = (187, 173, 160)
    cell = {
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
    font = {
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


class Text:
    def __init__(self, text, color):
        self.text_width, self.text_height = G.font.size(text)
        self.text = G.font.render(text, True, color)

    def draw(self, x, y):
        G.window.blit(self.text, (x, y))


class RoundedSquare:
    def __init__(self, a, r, color):
        self.a = a
        self.r = r
        self.color = color

    def draw(self, x, y):
        pygame.draw.rect(G.window, self.color, (x + self.r, y, self.a - 2 * self.r, self.a))
        pygame.draw.rect(G.window, self.color, (x, y + self.r, self.a, self.a - 2 * self.r))
        pygame.draw.circle(G.window, self.color, (x + self.r, y + self.r), self.r)
        pygame.draw.circle(G.window, self.color, (x + self.a - self.r, y + self.r), self.r)
        pygame.draw.circle(G.window, self.color, (x + self.a - self.r, y + self.a - self.r), self.r)
        pygame.draw.circle(G.window, self.color, (x + self.r, y + self.a - self.r), self.r)


class Cell:
    def __init__(self, value):
        self.value = value
        self.tile = RoundedSquare(G.cell_size - 2 * G.grid_spacing, G.radius, Colors.cell[value])
        if value:
            self.text = Text(str(value), Colors.font[value])

    def draw(self, x_real, y_real):
        self.tile.draw(x_real + G.grid_spacing, y_real + G.grid_spacing)
        if self.value:
            self.text.draw(x_real + (G.cell_size - self.text.text_width) / 2, y_real + (G.cell_size - self.text.text_height) / 2)


class Animation:
    def __init__(self, row_start, col_start, row_end, col_end, value):
        self.value = value
        self.row_start = row_start
        self.col_start = col_start
        self.row_end = row_end
        self.col_end = col_end
        self.move_distance_x = (col_end - col_start) * G.cell_size
        self.move_distance_y = (row_end - row_start) * G.cell_size
        self.move_step_x = self.move_distance_x // G.move_time
        self.move_step_y = self.move_distance_y // G.move_time
        self.start_pos_x = col_start * G.cell_size
        self.start_pos_y = row_start * G.cell_size

    def draw(self):
        pos_now_x = self.start_pos_x + self.move_step_x * (G.move_time - G.move_time_remaining)
        pos_now_y = self.start_pos_y + self.move_step_y * (G.move_time - G.move_time_remaining)

        G.CellsPrerendered[self.value].draw(pos_now_x, pos_now_y)

    def __repr__(self):
        return f"Anim(start=({self.row_start}, {self.col_start}, dist=({self.col_end - self.col_start}, {self.row_end - self.row_start}))"


class Game:
    debug_headless = False
    debug_anim = False
    debug_exit_status = None

    size = 4
    cell_size = 120
    radius = 9
    grid_spacing = 6
    fps = 60
    values = [0] + [2 ** i for i in range(1, 11 + 1)]

    def __init__(self):
        self.M = [[0 for _ in range(self.size)] for _ in range(self.size)]  # Matrix
        self.spawn_cell()
        self.spawn_cell()
        self.reset_animations()

    def start(self):
        self.move_time = 60 if self.debug_anim else 20
        self.reset_animations()
        pygame.display.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.size * self.cell_size, self.size * self.cell_size), vsync=1)
        pygame.display.set_caption("2048")
        self.font = pygame.font.Font("OpenSans-Bold.ttf", 52)
        self.CellsPrerendered = {i: Cell(i) for i in self.values}

        self.main_loop()

        pygame.quit()

    def main_loop(self):
        self.game_notOver = True
        self.move_time_remaining = 0
        dir_x, dir_y = 0, 0
        while self.game_notOver:
            self.clock.tick(self.fps)

            keys = pygame.key.get_pressed()
            # mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.game_notOver = False

            if self.move_time_remaining == 0:
                if self.cells_being_animated:  # something has moved
                    self.reset_animations()
                    self.spawn_cell()

                pressed_key = True
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # ←
                    dir_x, dir_y = -1, 0
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # →
                    dir_x, dir_y = 1, 0
                elif keys[pygame.K_UP] or keys[pygame.K_w]:  # ↑
                    dir_x, dir_y = 0, -1
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:  # ↓
                    dir_x, dir_y = 0, 1
                else:
                    pressed_key = False

                if pressed_key:
                    self.move_time_remaining = self.move_time
                    self.move_matrix(dir_x, dir_y)

                if self.debug_anim and (keys[pygame.K_y] or keys[pygame.K_n]):
                    self.debug_exit_status = keys[pygame.K_y]
                    self.game_notOver = False
            else:
                self.move_time_remaining -= 1

            self.redraw()

    def redraw(self):
        G.window.fill(Colors.board_background)

        for row, row_of_cells in enumerate(self.M):
            for col, val in enumerate(row_of_cells):
                if (row, col) in self.cells_being_animated:
                    G.CellsPrerendered[0].draw(col * self.cell_size, row * self.cell_size)
                else:
                    G.CellsPrerendered[val].draw(col * self.cell_size, row * self.cell_size)

        for anim in self.animations:
            anim.draw()

        pygame.display.update()

    def spawn_cell(self):
        if not self.debug_anim:
            free_tiles = [(row, col) for row, row_of_cells in enumerate(self.M) for col, val in enumerate(row_of_cells) if val == 0]
            row, col = random.choice(free_tiles)
            self.M[row][col] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])

    def reset_animations(self):
        self.animations = set()
        self.cells_being_animated = set()

    def add_animation(self, row_start, col_start, row_end, col_end, value):
        if not self.debug_headless:
            self.animations.add(Animation(row_start, col_start, row_end, col_end, value))
            self.cells_being_animated.add((row_end, col_end))

    def move_cell(self, row_start, col_start, row_end, col_end):
        self.add_animation(row_start, col_start, row_end, col_end, self.M[row_start][col_start])
        self.M[row_end][col_end] = self.M[row_start][col_start]
        self.M[row_start][col_start] = 0

    def merge_cells(self, row_absorbent, col_absorbent, row_absorbed, col_absorbed):
        if not self.debug_headless:
            # ↓ absorbent animation, check if absorbent is not already being moved
            if (row_absorbent, col_absorbent) not in self.cells_being_animated:
                self.add_animation(row_absorbent, col_absorbent, row_absorbent, col_absorbent, self.M[row_absorbent][col_absorbent])
            # ↓ absorbed animation
            self.add_animation(row_absorbed, col_absorbed, row_absorbent, col_absorbent, self.M[row_absorbed][col_absorbed])

        self.M[row_absorbent][col_absorbent] *= 2
        self.M[row_absorbed][col_absorbed] = 0
        self.no_longer_mergeable.add((row_absorbent, col_absorbent))

    def find_maximum_movement(self, row_start, col_start, dir_x, dir_y):
        if dir_x != 0:  # x direction
            col_end = col_start + dir_x
            while 0 < col_end < self.size - 1 and self.M[row_start][col_end] == 0 and (self.M[row_start][col_end + dir_x] == 0 or self.M[row_start][col_start] == self.M[row_start][col_end + dir_x]) and (row_start, col_end + dir_x) not in self.no_longer_mergeable:
                col_end += dir_x
            return col_end
        else:  # y direction
            row_end = row_start + dir_y
            while 0 < row_end < self.size - 1 and self.M[row_end][col_start] == 0 and (self.M[row_end + dir_y][col_start] == 0 or self.M[row_start][col_start] == self.M[row_end + dir_y][col_start]) and (row_end + dir_y, col_start) not in self.no_longer_mergeable:
                row_end += dir_y
            return row_end

    def move_matrix(self, dir_x, dir_y):
        self.no_longer_mergeable = set()
        if dir_x != 0:  # x direction
            for row in range(0, self.size):
                for col_start in (range(self.size - 2, -1, -1) if dir_x > 0 else range(0, self.size)):
                    if self.M[row][col_start] and not ((col_start == 0 and dir_x < 0) or (col_start == self.size - 1 and dir_x > 0)):
                        col_end = self.find_maximum_movement(row, col_start, dir_x, dir_y)
                        if self.M[row][col_end] == 0:
                            self.move_cell(row, col_start, row, col_end)
                        elif self.M[row][col_start] == self.M[row][col_end] and (row, col_end) not in self.no_longer_mergeable:
                            self.merge_cells(row, col_end, row, col_start)
        else:  # y direction
            for col in range(0, self.size):
                for row_start in (range(self.size - 2, -1, -1) if dir_y > 0 else range(0, self.size)):
                    if self.M[row_start][col] and not ((row_start == 0 and dir_y < 0) or (row_start == self.size - 1 and dir_y > 0)):
                        row_end = self.find_maximum_movement(row_start, col, dir_x, dir_y)
                        if self.M[row_end][col] == 0:
                            self.move_cell(row_start, col, row_end, col)
                        elif self.M[row_start][col] == self.M[row_end][col] and (row_end, col) not in self.no_longer_mergeable:
                            self.merge_cells(row_end, col, row_start, col)


G = Game()
if __name__ == "__main__":
    G.start()
