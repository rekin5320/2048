import unittest

import game2048

G = game2048.G


class TestMoving(unittest.TestCase):
    def test_1(self):
        G.M = [[2, 8, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 8, 0, 64]]
        G.move_matrix(0, -1)
        self.assertEqual([[2, 8, 8, 8], [128, 16, 64, 4], [0, 32, 0, 64], [0, 8, 0, 0]], G.M)
        G.move_matrix(1, 0)
        self.assertEqual([[0, 2, 8, 16], [128, 16, 64, 4], [0, 0, 32, 64], [0, 0, 0, 8]], G.M)
        G.move_matrix(1, 0)
        self.assertEqual([[0, 2, 8, 16], [128, 16, 64, 4], [0, 0, 32, 64], [0, 0, 0, 8]], G.M)

    def test_2(self):
        G.M = [[2, 8, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 8, 0, 64]]
        G.move_matrix(1, 0)
        self.assertEqual([[0, 0, 2, 16], [0, 16, 64, 8], [0, 128, 32, 4], [0, 0, 8, 64]], G.M)

    def test_3(self):
        G.M = [[2, 8, 8, 0], [0, 16, 64, 8], [128, 32, 0, 4], [0, 8, 0, 64]]
        G.move_matrix(0, -1)
        self.assertEqual([[2, 8, 8, 8], [128, 16, 64, 4], [0, 32, 0, 64], [0, 8, 0, 0]], G.M)
        G.move_matrix(-1, 0)
        self.assertEqual([[2, 16, 8, 0], [128, 16, 64, 4], [32, 64, 0, 0], [8, 0, 0, 0]], G.M)
        G.move_matrix(0, 1)
        self.assertEqual([[2, 0, 0, 0], [128, 0, 0, 0], [32, 32, 8, 0], [8, 64, 64, 4]], G.M)
        G.move_matrix(-1, 0)
        self.assertEqual([[2, 0, 0, 0], [128, 0, 0, 0], [64, 8, 0, 0], [8, 128, 4, 0]], G.M)
        G.move_matrix(0, -1)
        self.assertEqual([[2, 8, 4, 0], [128, 128, 0, 0], [64, 0, 0, 0], [8, 0, 0, 0]], G.M)
        G.move_matrix(-1, 0)
        self.assertEqual([[2, 8, 4, 0], [256, 0, 0, 0], [64, 0, 0, 0], [8, 0, 0, 0]], G.M)

    def test_4(self):
        G.M = [[2, 2, 2, 2] for _ in range(4)]
        G.move_matrix(0, 1)
        self.assertEqual([[0, 0, 0, 0], [0, 0, 0, 0], [4, 4, 4, 4], [4, 4, 4, 4]], G.M)
        G.move_matrix(0, -1)
        self.assertEqual([[8, 8, 8, 8], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], G.M)
        G.move_matrix(-1, 0)
        self.assertEqual([[16, 16, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], G.M)
        G.move_matrix(1, 0)
        self.assertEqual([[0, 0, 0, 32], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], G.M)
