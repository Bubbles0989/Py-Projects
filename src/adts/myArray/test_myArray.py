import unittest
from myArray import Array

class myArrayTest(unittest.TestCase):
    def setUp(self):
        self._array = Array(5)
        for i in range(5):
            self._array[i] = i

    def test_array_init_with_initial_size(self):
        array_size = len(self._array)
        self.assertEqual(5, array_size)

    def test_array_init_with_invalid_instance(self):
        with self.assertRaises(TypeError):
            error_array = Array(instance = 'string')

    def test_clone_raise_exception(self):
        with self.assertRaises(Exception):
            error_clone = Array.clone('string')

    def test_clone_valid_instance(self):
        clone_array = Array.clone(self._array)
        self.assertEqual(self._array, clone_array)

    def test_getitem_invalid_below_raises(self):
        with self.assertRaises(IndexError):
            error_getitem = self._array[-1]

    def test_getitem_invalid_above_raises(self):
        with self.assertRaises(IndexError):
            error_getitem = self._array[6]

    def test_setitem_invalid_above_raises(self):
        with self.assertRaises(IndexError):
            self._array[6] = 4

    def test_setitem_invalid_below_raises(self):
        with self.assertRaises(IndexError):
            self._array[-10] = 4

    def test_resize_with_shrinking_array(self):
        resize_array = Array(10)
        resize_array.resize(5)

        self.assertEqual(5, len(resize_array))

    def test_resize_with_expanding_array(self):
        resize_array = Array(5)
        resize_array.resize(10)

        self.assertEqual(10, len(resize_array))

    def test_resize_data_integrity(self):
        shrinking_array = Array(10)
        for i in range(10):
            shrinking_array[i] = i
        shrinking_array.resize(5)

        expanding_array = Array(5)
        for i in range(5):
            expanding_array[i] = i
        expanding_array.resize(10)

        for i in range(5):
            self.assertEqual(i, shrinking_array[i])

        for i in range(5):
            self.assertEqual(i, expanding_array[i])

    def test_iter(self):
        counter = 0
        for item in self._array:
            self.assertEqual(counter, item)
            counter += 1

        