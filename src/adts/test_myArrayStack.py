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

    