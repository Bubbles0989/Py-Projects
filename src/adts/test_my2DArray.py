import unittest
from my2DArray import Array2D

class my2DArrayTest(unittest.TestCase):
    def setUp(self):
        self._test_array = Array2D(3, 3)
        count = 0
        for row in range(self._test_array.row_len):
            for col in range(self._test_array.column_len):
                self._test_array[row][col] = count
                count += 1

    def test_init_with_rows_len(self):
        test_array2d = Array2D(4, 3)
        row_len = test_array2d.row_len
        self.assertEqual(4, row_len)

    def test_init_with_col_len(self):
        test_array2d = Array2D(4, 3)
        col_len = test_array2d.column_len
        self.assertEqual(3, col_len)

    def test_clone_valid(self):
        test_array_clone = Array2D.clone(self._test_array)
        self.assertEqual(self._test_array, test_array_clone)