"""
PyQueue implements basically queue in Python for educational purposes.
Queues are implemented with a class based on built-in `list` class.

Author: Matthieu BOUCHET
Author email: matthieu.bouchet@outlook.com
License: MIT LICENSE

MIT License

Copyright (c) 2021 Matthieu BOUCHET

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class Queue(list):
    """
    Queue class is implemented with this class.
    Founded on list class
    """

    def __init__(self,listEl = None, maxLen = -1) -> bool:
        """Constructor of class

        Args:
            listEl (iterable, optional): Iterable to build a queue. Defaults to None.
            maxLen (integer, optional): Maximum length of Queue. If -1, unlimited. Defaults to -1.
        """
        self.maxLength = maxLen
        if type(self.maxLen) == int:
            raise TypeError('Maximum length specified must be an integer')
        if self.maxLen() == 0 or (self.maxLen() < 0 and self.maxLen() != -1):
            raise ValueError('Queue can not be have 0 max length')


        if listEl is not None:
            try:
                pass
                return True
            except TypeError:
                return False

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
    
    def pop(self):
        """
        Overload of pop list method
        """
        if self.isEmpty():
            raise QueueIsEmpty

        return super().pop(0)

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
        super().__init__('Queue is empty, it\'s impossible to remove an element')

pass