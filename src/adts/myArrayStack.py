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
        pass

    def pop(self):
        pass

    def clear(self):
        pass

    @property
    def top(self):
        pass

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