import unittest

from Poker import get_same_number,Poker,get_kind_rank

class TestPoker(unittest.TestCase):

    def test_kind_1(self):
        assert get_kind_rank(['2H','3D','5S','9C','KD']) == 1

    def test_kind_2(self):
        assert get_kind_rank(['2H','2D','5S','9C','KD']) == 2

    def test_kind_3(self):
        assert get_kind_rank(['2H','2D','5S','5C','KD']) == 3

    def test_kind_4(self):
        assert get_kind_rank(['2H','2D','2S','9C','KD']) == 4

    def test_kind_5(self):
        assert get_kind_rank(['2H','3D','5S','4C','6D']) == 5

    def test_kind_6(self):
        assert get_kind_rank(['2S','8S','AS','QS','3S']) == 6

    def test_kind_7(self):
        assert get_kind_rank(['2H','2D','2S','9C','9D']) == 7

    def test_kind_8(self):
        assert get_kind_rank(['2H','2D','2S','2C','KD']) == 8

    def test_kind_9(self):
        assert get_kind_rank(['2H','3H','5H','6H','4H']) == 9


    def test_high_card(self):
        assert Poker("Black:2H 3D 5S 9C KD;White:2C 3H 4S 8C AH") == "White wins"

    def test_two_kind(self):
        assert Poker("Black:2H 4S 4C 2D 4H;White:2S 8S AS QS 3S") == "Black wins"

    def test_pair(self):
        assert Poker("Black:2H 2D 5S 9C KD;White:2C 2S 4S KC 8H") == "Black wins"

    def test_two_pairs(self):
        assert Poker("Black:2H 2D 4S 4C KD;White:2S 2C 4D 4H KH") == "Tie"

    def test_three_of_a_kind(self):
        assert Poker("Black:2H 2D 3S 2C KD;White:2S 4H 4C 4S KH") == "White wins"

    def test_straight(self):
        assert Poker("Black:2H 3D 4S 5C 6D;White:TD JH QC KS AH") == "White wins"

    def test_flush(self):
        assert Poker("Black:2H 5H 7H 9H QH;White:3H 8H QH KH AH") == "White wins"

    def test_full_hose(self):
        assert Poker("Black:2H KD KS 2S KH;White:3D 8H 8C 8S 3H") == "Black wins"

    def test_four_of_a_kind(self):
        assert Poker("Black:6H 6D 3S 6S 6C;White:8D 8H 8C 8S 3H") == "White wins"

    def test_straight_flush(self):
        assert Poker("Black:5H 6H 7H 8H 9H;White:3D 4D 5D 6D 7D") == "Black wins"

if __name__ == "__main__":
    unittest.main()