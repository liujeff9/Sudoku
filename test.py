import unittest 
from solve import Board 
from puzzles import easy 

class Test(unittest.TestCase):
    
    def setUp(self):
        self.board = Board(easy)

    def test_in_col(self):
        valid = self.board.valid_col(0, 8)
        self.assertFalse(valid)

    def test_not_in_col(self):
        valid = self.board.valid_col(0, 5)
        self.assertTrue(valid)

    def test_in_row(self):
        valid = self.board.valid_row(0, 3)
        self.assertFalse(valid)

    def test_not_in_row(self):
        valid = self.board.valid_row(0, 6)
        self.assertTrue(valid)

    def test_in_square(self):
        valid = self.board.valid_square(8, 8, 5)
        self.assertFalse(valid)

    def test_not_in_square(self):
        valid = self.board.valid_square(8, 7, 6)
        self.assertTrue(valid)

if __name__ == '__main__': 
    unittest.main() 