from myArray import Array 

class ArrayStack:
    """ Class ArrayStack - representing a fixed-size stack using a 1D Array"""

    def __init__(self, max_size: int = 0, instance=None) -> None:
        """ Constructor
            Usage:  stack = ArrayStack(10)
        """

        self._max_size = max_size
        self._stack = Array(max_size)
        self._top = 0

        if not isinstance(instance, ArrayStack) and instance != None:
            raise TypeError('instance is not an Array')
        
        if instance != None:
            for index in instance.stack():
                self._stack[index] = instance.stack()[index]
        
    @staticmethod
    def clone(instance):
        if instance is not None and not isinstance(instance, ArrayStack):
            raise TypeError('instance is not an array')
        
        clone = ArrayStack(instance.size)

        for index in instance._stack:
            clone.push(index)

        return clone

    def push(self, item):
        if self.full:
            raise IndexError('stack is full')
        
        self._stack[self._top] = item
        self._top += 1

    def pop(self):
        if self.empty:
            raise IndexError('stack is empty')
        
        temp_stack_top = self._stack[self._top - 1]
        self._stack.resize(self._max_size - 1)
        self._top -= 1

        return temp_stack_top

    def clear(self):
        Array.clear(self._stack)
        self._top = 0

    @property
    def top(self):
        if self.empty:
            raise IndexError("stack is empty")
        
        return self._stack[self._top - 1]

    @property
    def size(self) -> int:
        return len(self._stack)

    @property
    def full(self) -> bool:
        if self._top == self._max_size:
            return True
        
        return False

    @property
    def empty(self) -> bool:
        if len(self._stack) == 0:
            return True

        if self._top == 0:
            return True
        
        return False

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArrayStack):
            return False

        if other.size < self.size or other.size > self.size:
            return False

        return self._stack == other._stack  

    def __len__(self) -> int:
        return self._max_size

    def __str__(self) -> str:
        return f'Top : {self.top}, for array stack: {str(self._stack)}'

    def stack(self):
        return self._stack   