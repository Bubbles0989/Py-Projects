
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

        return copy

    def __getitem__(self, index: int):
        if index >= len(self._items):
            raise IndexError('Above Bounds.')
        
        if index < 0:
            raise IndexError("Below Bounds.")
        
        return self._items[index]

    def __setitem__(self, index: int, data) -> None:
        if index >= len(self._items) or index < 0:
            raise IndexError('Out of Bounds.')

        self._items[index] = data

    def __len__(self) -> int:
        return len(self._items)

    def resize(self, new_size: int) -> None:
        new_items = [None] * new_size

        smaller_size = len(self._items) if len(self._items) <= new_size else new_size

        for i in range(smaller_size):
            new_items[i] = self._items[i]

        self._items = new_items

    def __eq__(self, other) -> bool:
        if not isinstance(other, Array):
            return False
        
        return self._items == other._items

    def __iter__(self):
        for i in range(len(self._items)):
            yield self._items[i]

    def __delitem__(self, index: int) -> None:
        del self._items[index]

    def __contains__(self, item) -> bool:
        if item in self._items:
            return True
        
        return False

    def clear(self) -> None:
        self._items = [None] * len(self._items)

    @staticmethod
    def to_array(lst: list):
        array = Array(len(lst))

        for i in range(len(lst)):
            array[i] = lst[i]

        return array

    def __str__(self) -> str:
        return str(self._items)
    
    def merge(self, other):
        pass

    
            