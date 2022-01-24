import unittest

import game2048


class TestMoving(unittest.TestCase):
    def test_1(self):
        game2048.Matrix = [[2, 8, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 8, 0, 64]]
        game2048.move_cells(0, -1)
        self.assertEqual([[2, 8, 8, 8], [128, 16, 64, 4], [0, 32, 0, 64], [0, 8, 0, 0]], game2048.Matrix)
        game2048.move_cells(1, 0)
        self.assertEqual([[0, 2, 8, 16], [128, 16, 64, 4], [0, 0, 32, 64], [0, 0, 0, 8]], game2048.Matrix)
        game2048.move_cells(1, 0)
        self.assertEqual([[0, 2, 8, 16], [128, 16, 64, 4], [0, 0, 32, 64], [0, 0, 0, 8]], game2048.Matrix)

    def test_2(self):
        game2048.Matrix = [[2, 8, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 8, 0, 64]]
        game2048.move_cells(1, 0)
        self.assertEqual([[0, 0, 2, 16], [0, 16, 64, 8], [0, 128, 32, 4], [0, 0, 8, 64]], game2048.Matrix)

    def test_3(self):
        game2048.Matrix = [[2, 8, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 8, 0, 64]]
        game2048.move_cells(0, -1)
        self.assertEqual([[2, 8, 8, 8], [128, 16, 64, 4], [0, 32, 0, 64], [0, 8, 0, 0]], game2048.Matrix)
        game2048.move_cells(-1, 0)
        self.assertEqual([[2, 16, 8, 0], [128, 16, 64, 4], [32, 64, 0, 0], [8, 0, 0, 0]], game2048.Matrix)
        game2048.move_cells(0, 1)
        self.assertEqual([[2, 0, 0, 0], [128, 0, 0, 0], [32, 32, 8, 0], [8, 64, 64, 4]], game2048.Matrix)
        game2048.move_cells(-1, 0)
        self.assertEqual([[2, 0, 0, 0], [128, 0, 0, 0], [64, 8, 0, 0], [8, 128, 4, 0]], game2048.Matrix)
        game2048.move_cells(0, -1)
        self.assertEqual([[2, 8, 4, 0], [128, 128, 0, 0], [64, 0, 0, 0], [8, 0, 0, 0]], game2048.Matrix)
        game2048.move_cells(-1, 0)
        self.assertEqual([[2, 8, 4, 0], [256, 0, 0, 0], [64, 0, 0, 0], [8, 0, 0, 0]], game2048.Matrix)

    def test_4(self):
        game2048.Matrix = [[2, 2, 2, 2] for _ in range(4)]
        game2048.move_cells(0, 1)
        self.assertEqual([[0, 0, 0, 0], [0, 0, 0, 0], [4, 4, 4, 4], [4, 4, 4, 4]], game2048.Matrix)
        game2048.move_cells(0, -1)
        self.assertEqual([[8, 8, 8, 8], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], game2048.Matrix)
        game2048.move_cells(-1, 0)
        self.assertEqual([[16, 16, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], game2048.Matrix)
        game2048.move_cells(1, 0)
        self.assertEqual([[0, 0, 0, 32], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], game2048.Matrix)
