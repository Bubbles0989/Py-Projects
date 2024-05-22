
class Array: 

    def __init__(self, size: int = 0, instance=None) -> None:
        if instance is not None:
            if not isinstance(instance, Array):
                raise TypeError('Instance is not an Array Object.')
            self._items = [None] * len(instance)
            for i in range(len(instance)):
                self._items[i] = instance[i]
        else:
            self._items = [None] * size

    @staticmethod
    def clone(instance):
        if not isinstance(instance, Array):
            raise TypeError('Instance is not an Array Object.')
        
        copy = Array(len(instance))

        for i in range(len(instance)):
            copy[i] = instance[i]

    def __getitem__(self, index: int):
        if index >= len(self._items):
            raise IndexError('Above Bounds.')
        
        if index <= len(self._items):
            raise IndexError("Below Bounds.")
        
        return self._items[index]

    def __setitem__(self, index: int, data) -> None:
        if index >= len(self._items) or index <= len(self._items):
            raise IndexError('Out of Bounds.')

        self._items[index] = data

    def __len__(self) -> int:
        pass

    def resize(self, new_size: int) -> None:
        pass

    def __eq__(self, other) -> bool:
        pass

    def __iter__(self):
        pass

    def __delitem__(self, index: int) -> None:
        pass

    def __contains__(self, item) -> bool:
        pass

    def clear(self) -> None:
        pass

    @staticmethod
    def to_array(lst: list):
        pass

    def __str__(self) -> str:
        pass
    
    def merge(self, other):
        pass

    
            