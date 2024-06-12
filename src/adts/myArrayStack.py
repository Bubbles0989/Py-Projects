from myArray import Array 

class ArrayStack:

    def __init__(self, max_size: int = 0, instance=None) -> None:
        self._max_size = max_size
        self._stack = Array(max_size)
        self._top = 0

        if not isinstance(instance, Array) and instance != None:
            raise TypeError('instance is not an Array')
        
    @staticmethod
    def clone(instance):
        if instance is not None and not isinstance(instance, Array):
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
        pass

    @property
    def full(self) -> bool:
        pass

    @property
    def empty(self) -> bool:
        pass  

    def __eq__(self, other) -> bool:
        pass  

    def __len__(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    def stack(self):
        pass   