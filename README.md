# PyDataStructures
Basic library to implement data structures in Python.

Data structures availables are :

* Queues

## Installation

### Pip (*PyPi*)

To install with *pip* via *PyPi*, you can type this command :

```
pip install -i https://test.pypi.org/simple/ pydatastructures
```

### Via source code

The source code is available on [GitHub](https://github.com/MatthieuBOUCHET/PyDataStructures). To clone the repository, you can type this command :

```
git clone https://github.com/MatthieuBOUCHET/PyDataStructures.git
```



## Queues

A class `Queue` is available to implement queues. This class is based on `list` built-in class.

### Creation examples

```python
import pydatastructures.queue as queue

#Create a queue
q = queue.Queue()
#This queue have an unlimited length and is empty
```

#### Create a queue with a maximum length defined

```python
import pydatastructures.queue as queue

#Create a queue
q = queue.Queue(maxLen=10)
#This queue have a maximum length of 10 and is empty
```

#### Create a queue from an iterable element

```python
import pydatastructures.queue as queue

l = ['a','b','c','d']
#Create a queue from list l

q = queue.Queue(listEl=l)
#This queue have an unlimited length and is created from list l

>>> print q
'a' | 'b' | 'c' | 'd'
```

### Use examples

#### Add element
Add an element at the end of queue.

Two methods exist to add an element in queue

* `append(element)`
* `addQueue(element)`

Two methods are **equivalent**.

```python
import pydatastructures.queue as queue

q = queue.Queue()

q.addQueue('a')
#OR
q.append('a')

q.addQueue('b')
q.addQueue('c')

>>> print q
'a' | 'b' | 'c'
```

#### Remove element
Remove first element of queue.

Two methods exist to add an element in queue

* `pop()`
* `removeQueue()`

Two methods are **equivalent**.

```python
import pydatastructures.queue as queue

q = queue.Queue(listEl=['a','b','c'])

>>> print q
'a' | 'b' | 'c'

a = q.removeQueue()

>>> print q
'b' | 'c'
>>> print a
'a

b = q.removeQueue()

>>> print q
'c'
>>> print b
'b'
```



### Exceptions

#### *QueueOverflow*

Exception raised if queue maximum length is exceeded.

```python
import pydatastructures.queue as queue

q = queue.Queue(maxLen=1)
q.addQueue('a')

>>> print q
'a'

q.addQueue('b')
#Max len is 1, and we try to have 2 elements in queue
QueueOverflow: Queue maximum length is exceeded
```

#### *QueueIsEmpty*

Exception raised if we try to remove an element from an empty queue.

```python
import pydatastructures.queue as queue

q = queue.Queue()
q.addQueue('a')
q.addQueue('b')

>>> print q
'a' | 'b'

q.removeQueue()
q.removeQueue()
>>> print q
Empty queue !

>>> q.removeQueue()
QueueIsEmpty:Queue is empty, it is impossible to remove an element
```