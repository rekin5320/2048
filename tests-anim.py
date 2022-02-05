import unittest

import game2048

G = game2048.G
G.debug_anim = True
G.size = 4


class TestAnimation(unittest.TestCase):
    def test_1(self):
        print("\n↑")
        G.M = [[0, 0, 0, 0], [16, 0, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0]]
        G.start()
        self.assertTrue(G.debug_exit_status)

    def test_2(self):
        print("\n↓")
        G.M = [[4, 0, 0, 0], [4, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]]
        G.start()
        self.assertTrue(G.debug_exit_status)

    def test_3(self):
        print("\n↑")
        G.M = [[2, 0, 0, 0], [2, 0, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0]]
        G.start()
        self.assertTrue(G.debug_exit_status)

    def test_4(self):
        print("\n→")
        G.M = [[4, 4, 2, 2], [0, 0, 0, 0], [2, 2, 4, 4], [0, 0, 0, 0]]
        G.start()
        self.assertTrue(G.debug_exit_status)

    def test_5(self):
        print("\n←")
        G.M = [[4, 4, 2, 2], [0, 0, 0, 0], [2, 2, 4, 4], [0, 0, 0, 0]]
        G.start()
        self.assertTrue(G.debug_exit_status)
