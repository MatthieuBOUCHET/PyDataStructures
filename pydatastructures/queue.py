"""
PyQueue implements basically queue in Python for educational purposes.
Queues are implemented with a class based on built-in `list` class.

Author: Matthieu BOUCHET
Author email: matthieu.bouchet@outlook.com
License: MIT LICENSE
"""

class Queue(list):
    """
    Queue class is implemented with this class.
    Based on list built-in class
    """

    def __init__(self,listEl = None, maxLen = -1) -> bool:
        """Constructor of class

        Args:
            listEl (iterable, optional): Iterable to build a queue. Defaults to None.
            maxLen (integer, optional): Maximum length of Queue. If -1, unlimited. Defaults to -1.
        """
        self.maxLength = maxLen

        if type(self.maxLength) != int:
            raise TypeError('Maximum length specified must be an integer')
        if self.maxLen() == 0 or (self.maxLen() < 0 and self.maxLen() != -1):
            raise ValueError('Queue can not be have 0 max length')


        if listEl is not None:
            try:
                for el in listEl:
                    self.append(el)
                    
            except TypeError:
                raise TypeError('listEl must be an iterable')

    def len(self) -> int:
        """
        Return length of queue (integer)
        """
        return len(self)

    def maxLen(self) -> int:
        """Return maximum length of queue.
        If queue has an unlimited length, return -1

        Returns:
            int: Maximum length
        """
        return self.maxLength

    def isEmpty(self) -> bool:
        """Return if a queue is empty or not.

        Returns:
            bool: True => empty
        """
        return self.len() == 0

    def append(self, __object) -> None:
        """
        Overload of append list method
        """
        if self.len() >= self.maxLen():
            if self.maxLen() != -1:
                raise QueueOverflow

        return super().append(__object)
    
    def addQueue(self, el) -> None:
        """
        Aliase append method
        """
        return self.append(el)
    
    def pop(self):
        """
        Overload of pop list method
        """
        if self.isEmpty():
            raise QueueIsEmpty

        return super().pop(0)
    
    def removeQueue(self):
        """
        Aliase pop method
        """
        return self.pop()
    
    def __str__(self) -> str:
        stringReturn = ''
        if self.isEmpty():
            return 'Empty queue !'
        
        for el in range(self.len()):
            stringReturn += str(self[el])
            if el == self.len() - 1:
                return stringReturn
            
            stringReturn += ' | '
    
    def __repr__(self) -> str:
        return self.__str__()

class QueueOverflow(Exception):
    """
    Exception raised if queue maximum length is exceeded
    """
    def __init__(self) -> None:
        super().__init__('Queue maximum length is exceeded')

class QueueIsEmpty(Exception):
    """
    Exception raised if queue is empty and when it's impossible to remove an element
    """
    def __init__(self) -> None:
        super().__init__('Queue is empty, it is impossible to remove an element')

pass