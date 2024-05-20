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
        