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
