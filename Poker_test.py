import unittest

import Poker


class TestPoker(unittest.TestCase):
    def test_1(self):
        assert Poker("Black:2H 3D 5S 9C KD;White:2C 3H 4S 8C AH") == "White wins"

    def test_2(self):
        assert Poker("Black:2H 4S 4C 2D 4H;White:2S 8S AS QS 3S") == "Black wins"

    def test_3(self):
        assert Poker("Black:2H 3D 5S 9C KD;White:2C 3H 4S 8C KH") == "Black wins"

    def test_4(self):
        assert Poker("Black:2H 3D 5S 9C KD;White:2D 3H 5C 9S KH") == "Tie"


if __name__ == "__main__":
    unittest.main()