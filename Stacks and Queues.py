#Stacks and Queues

#A stack is a last-in-first out LIFO data structure. You can push things nto the stack, and whatever the last item that was
#pushed onto the stack is the first one you'll pop off.

class Stack:
    """A last in, first out sequence of items"""
    #Private attributes:
    #.itemlist (a list)

    def __init__(self, items=None):
        """Initializes self with the given iterable items
        Stack, iterable -> None"""

        if items == None:
            self._itemlist = []
        else:
            self._itemlist = list(items)

    def __repr__(self):
        """Returns a string of the form Stack(itemlist)
        Stack -> Str"""
        return "Stack("+repr(self._itemlist) + ")"

    def push(self, item):
        """Pushes item onto the top of the stack self
        Stack, object -> None"""
        self._itemlist.append(item)

    #Quiz 12B

##    def pop(self):
##        """Returns and removes the last item in the stack self
##        Stack, object -> Object"""
##        temp = self._itemlist[-1]
##        del self._itemlist[-1]
##        return temp

    def pop(self):
        """Returns and removes the last item in the stack self
        Stack, object -> Object"""
        #Right way
        return self._itemlist.pop()

#A queue is a first in first out, FIFO data structure. You can enqueue an item by putting at the end of the queue
# and you can deqeue an item by removing from the front of the queue.

class Queue:
    """A first in first out sequence of items"""
    #Private attributes
    #._itemlist (a list)

    def __init__(self, items=None):
        """Initializes self as a list with the given item
        Queue, Some items -> None"""
        if items == None:
            self._itemlist = []
        else:
            self._itemlist = list(items)

    def __repr__(self):
        """Returns a string in the form Queue(itemlist)
        Queue -> String"""
        return "Queue(" + repr(self._itemlist) + ")"

    def enqueue(self, item):
        """Add an item to the end of the queue
        Queue, object -> None"""
        self._itemlist.append(item)

    def dequeue(self):
        """Removes and returns the item at the front of the queue
        Queue -> Object of x type"""
        temp = self._itemlist[0]
        del self._itemlist[0]
        return temp


#################
#A Graph is a collection of nodes and a collection of pairs of nodes called edges, describing which nodes are neighbors
# of which other nodes

#A directed graph is similar to a graph, but the connections are directional.

#What are some ways we could store the data in a graph
#Method 1, A dictionary where the keys are the nodes and the values are lists of all the neighbors of that key node

#Method 1B, A dictionary where the keys are the nodes, and each value is a set of all the neighbors of that key node

#Method 2, A set of nodes and a set of two-item lists representing each of the edges.

#Method 3, Transition Matrix, a list of lists where each row and each column represents the single node, and 0 means
#no connection, and 1 means there is a connection/edge





    
        
    
