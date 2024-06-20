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
        clone_stack = ArrayStack.clone(self._test_stack)
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

        with self.assertRaises(IndexError):
            test_clear_array.top

    def test_top(self):
        self.assertEqual(self._test_stack.top, 9)

        empty_stack = ArrayStack(1)
        with self.assertRaises(IndexError):
            empty_stack.top

    def test_size(self):
        self.assertEqual(self._test_stack.size, 10)

    def test_full(self):
        self.assertTrue(self._test_stack.full)

        test_full_false = ArrayStack(10)
        for i in range(5):
            test_full_false.push(i)

        self.assertFalse(test_full_false.full)        
    
    def test_empty(self):
        test_empty_array = ArrayStack(10)
        self.assertTrue(test_empty_array.empty)
        self.assertFalse(self._test_stack.empty)

    def test_eq(self):
        self.assertFalse(self._test_stack == 'string')
        
        test_stack = ArrayStack(5)
        self.assertFalse(test_stack == self._test_stack)
        
        test_stack = ArrayStack(10, self._test_stack)
        self.assertTrue(test_stack == self._test_stack)