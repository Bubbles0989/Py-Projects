import unittest
from myArrayStack import ArrayStack

class myArrayStackTest(unittest.TestCase):
    def setUp(self):
        self._test_stack = ArrayStack(10)
        for i in range(10):
            self._test_stack.push(i)

    def test_init_raises(self):
        with self.assertRaises(TypeError):
            string = ArrayStack(1, 'string')

    def test_clone(self):
        clone_stack = self._test_stack.clone()
        self.assertEqual(clone_stack, self._test_stack)

        with self.assertRaises(TypeError):
            error_clone = self._test_stack.clone('string')

    def test_push(self):
        with self.assertRaises(IndexError):
            self._test_stack.push(1)

        test_correct_stack = ArrayStack(5)
        for index in range(len(test_correct_stack)):
            test_correct_stack.push(index)

        self.assertEqual(test_correct_stack.top, 4)

    def test_pop(self):
        empty_stack = ArrayStack(0)
        with self.assertRaises(IndexError):
            empty_stack.pop()

        self.assertEqual(self._test_stack.pop(), 9)

    def test_clear(self):
        test_clear_array = ArrayStack(5)
        for index in range(5):
            test_clear_array.push(index)

        test_clear_array.clear()

        self.assertEqual(test_clear_array.top, 0)

    def test_top(self):
        self.assertEqual(self._test_stack.top, 9)

        empty_stack = ArrayStack(1)
        with self.assertRaises(IndexError):
            empty_stack.top

    def test_size(self):
        self.assertEqual(self._test_stack.size, 10)
    