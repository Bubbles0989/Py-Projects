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
    