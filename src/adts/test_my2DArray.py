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

    def test_str(self):
        string = str(self._test_array)
        self.assertIsNotNone(string)

    def test_clear(self):
        self._test_array.clear()
        test_clear = self._test_array[1][1]
        self.assertEqual(None, test_clear)

    def test_resize_column_smaller(self):
        self._test_array.resize_columns(2)

        sum = 0
        for row in range(self._test_array.row_len):
            for col in range(self._test_array.column_len):
                sum += self._test_array[row][col]

        self.assertEqual(21, sum)

    def test_resize_column_larger(self):
        self._test_array.resize_columns(20)

        sum = 0
        for row in range(self._test_array.row_len):
            for col in range(self._test_array.column_len):
                if not self._test_array[row][col] == None:
                    sum += self._test_array[row][col]

        self.assertEqual(36, sum)

    def test_resize_row_smaller(self):
        self._test_array.resize_rows(2)

        sum = 0
        for row in range(self._test_array.row_len):
            for col in range(self._test_array.column_len):
                sum += self._test_array[row][col]

        self.assertEqual(21, sum)

    def test_resize_row_larger(self):
        self._test_array.resize_rows(4)

        sum = 0
        for row in range(self._test_array.row_len):
            for col in range(self._test_array.column_len):
                if not self._test_array[row][col] == None:
                    sum += self._test_array[row][col]

        self.assertEqual(33, sum)

    def test_set(self):
        self._test_array[1][1] = 3
        val = self._test_array[1][1]
        self.assertEqual(3, val)

    def test_set_index_error(self):
        with self.assertRaises(IndexError):
            self._test_array[8675][309] = 9

    def test_get_index_error(self):
        with self.assertRaises(IndexError):
            self._test_array.getitem(957, 747)

    def test_raise_type_error_clone(self):
        with self.assertRaises(TypeError):
            Array2D.clone('dabi confirmed as todoroki touya')