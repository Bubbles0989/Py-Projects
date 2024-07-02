from myArray import Array 


class Array2D:
    """ Class Array2D - representing 2D data using a 1D array"""

    class _Row:
        """ Private inner class _Row - represents a row in the 2D array""" 

        def __init__(self, array2D: 'Array2D', row_index: int) -> None:
            """ Constructor - represents a row in the 2D array
                Usage:  row = _Row(array2d, row_index)
            """         
            self._array2D = array2D
            self._row_index = row_index

        def __getitem__(self, col_index: int):
            """ Bracket operator for getting an item
                Usage: val = array2d[row_index][column_index]
            """
            return self._array2D.getitem(self._row_index, col_index)
        
        def __setitem__(self, col_index: int, data):
            """ Bracket operator for setting an item
                Usage: array2d[row_index][column_index] = val
            """    
            self._array2d.setitem(self._row_index, col_index, data)         
    
    def __init__(self, row_len: int = 0, col_len: int = 0, instance=None) -> None:
        """ Constructor
            Usage:  array = Array2D(10)
        """
        if instance is not None and not isinstance(instance, Array2D):
            raise TypeError('Instance is not an Array2D instance')
        
        self._items = Array(row_len * col_len)
        self._row_len = row_len
        self._col_len = col_len

    @staticmethod
    def clone(instance):
        """ Clone the array2d
            Usage:  array2d = Array2D.clone(instance)
        """     
        if instance is not None and not isinstance(instance, Array2D):
            raise TypeError('The instance is not a 2D Array')
        
        clone = Array2D(instance._row_len, instance._col_len)

        for index in range(len(instance._items)):
            clone._items[index] = instance._items[index]

        return clone
    
    def __getitem__(self, row_index: int):
        """ Bracket operator for getting an item
            Usage: val = array2d[row_index][column_index]
        """
        return self._Row(self, row_index)
    
    def getitem(self, row_index: int, col_index: int):
        """ Helper method for getting an item
            Usage: val = array2d.getitem(row_index, column_index)
        """
        if row_index < 0 or row_index >= self._row_len:
            raise IndexError(f'{row_index} is out of bounds for an Array2D with row size: {self.row_len}')
        
        actual_index_in_1 = (row_index * 3) + col_index
        return self._items[actual_index_in_1]
    
    def setitem(self, row_index: int, col_index: int, data) -> None:
        """ Helper method for setting an item
            Usage: array2d[row_index][column_index] = val
        """
        if row_index < 0 or row_index >= self._row_len:
            raise IndexError(f'{row_index} is out of bounds for an Array2D with row size: {self.row_len}')
        
        actual_index_in_1 = (row_index * 3) + col_index
        self._items[actual_index_in_1] = data