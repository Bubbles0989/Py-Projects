import unittest
from my2DArray import Array2D

class my2DArrayTest(unittest.TestCase):
    def setUp(self):
        self._test_array = Array2D(3, 3)
        count = 0
        for row in range(self._test_array.row_len):
            for col in range(self._test_array.col_len):
                self._test_array[row][col] = count
                count += 1

    def test_init_with_rows_len(self):
        test_array2d = Array2D(4, 3)
        row_len = test_array2d.row_len
        self.assertEqual(4, row_len)