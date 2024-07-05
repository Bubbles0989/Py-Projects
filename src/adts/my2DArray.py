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

    @property
    def column_len(self):
        """ len method for the length of the columns
            Usage: column_length = array2d.columns_len
        """
        return self._column_len
    
    @property
    def row_len(self):
        """ len method for the length of the rows
            Usage: row_length = array2d.rows_len
        """
        return self._row_len
    
    def resize_columns(self, new_col_len: int) -> None:
        """ Resize the length of the columns
            Usage: array2d.resize_columns(new_columns_len)
        """     

        if not isinstance(new_col_len, int):
            raise ValueError('New col length needs to be an int') 

        new_items = Array(self._row_len * new_col_len)  
        smaller_col_len = self._col_len if self._col_len < new_col_len else new_col_len

        for row_index in range(self._row_len):
            new_offset = row_index * new_col_len
            old_offset = row_index * self._column_len
            for col_index in range(smaller_col_len):
                new_items[new_offset + col_index] = self._items2d[old_offset + col_index]

        self._items2d = new_items
        self._row_len = new_col_len