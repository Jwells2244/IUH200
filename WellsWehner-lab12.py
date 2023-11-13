#Lab 12
class Stack:
    """A Last-In-First-Out sequence.

    public attributes:
        itemlist (a list)
    """
    
    def __init__(self, items=None):
        """Initializes self with the given iterable or with an empty stack.
        Stack, iterable -> None"""
        if items == None:
            self.itemlist = []
        else:
            self.itemlist = list(items)

    def __repr__(self):
        """Returns a string of the form Stack(itemlist)
        Stack -> str"""
        return "Stack(" + repr(self.itemlist) + ")"

    def push(self, item):
        """Adds item to the top of the Stack self.
        Stack, object -> None"""
        self.itemlist.append(item)

    def pop(self):
        """Removes and returns the item at the top of the Stack self.
        Stack -> object"""
        return self.itemlist.pop()

    def is_empty(self):
        """Determines whether the Stack self is empty or not.
        Stack -> bool"""
        return len(self.itemlist) == 0

class Queue:
    """A First-In-First-Out sequence.

    public attributes:
        itemlist (a list)
    """
    def __init__(self, items=None):
        """Initializes self with the given iterable or with an empty queue.
        Queue, iterable -> None"""
        if items == None:
            self.itemlist = []
        else:
            self.itemlist = items

    def __repr__(self):
        """Returns a string of the form Queue(itemlist)
        Queue -> str"""
        return "Queue(" + repr(self.itemlist) + ")"

    def enqueue(self, item):
        """Adds item to the end of the Queue self.
        Queue, object -> None"""
        self.itemlist.append(item)

    def dequeue(self):
        """Removes and returns the item at the front of the Queue self.
        Queue -> object"""
        item = self.itemlist[0]
        del self.itemlist[0]
        return item

    def is_empty(self):
        """Determines whether the Queue self is empty or not.
        Queue -> bool"""
        return len(self.itemlist) == 0


class WGraph:
    """A collection of vertices, called nodes, and a collection of directed edges that tell us which vertices
    are connected to other vertices. When two vertices are directly connected by an edge, we say that they are
    adjacent to one another. However, with these graphs, there is potentially paths to from one vertice to another, that
    don't exist in the vertice going back."""
    #Private Attributes:
    #dict: a dictionary

    def __init__(self, vertices={}):
        """Initializes self with the given inputs, vertices and edges
        WGraph, dict -> None"""
        self._dict = vertices

    def __repr__(self):
        """Returns a string in the form Graph(dict)
        WGraph -> String"""
        return "WGraph("+repr(self._dict)+")"

    def neighbors(self, vertex):
        """Takes the vertex and returns the set of the vertices that are adjacent to it
        WGraph, int -> Set or None if the vertex does not exist"""
        if vertex in self._dict:
            returnSet = set()
            for val in self._dict[vertex]:
                returnSet.add(val)
            return returnSet
        else:
            return None
        
    def neighbors_with_weight(self, vertex):
        """Takes the vertex and returns the set of the vertices with the weight values attached, that are adjacent to it
        WGraph, int -> Set or None if the vertex does not exist"""
        if vertex in self._dict:
            return self._dict[vertex]
        else:
            return None
      
    def is_adjacent_to(self, vert1, vert2):
        """Takes two vertices, vert1 and vert2, and determines whether they are adjacent to each other in the graph
        WGraph, int, int -> Boolean"""
        neighbors1 = WGraph.neighbors(self, vert1)
        neighbors2 = WGraph.neighbors(self, vert2)
        if vert2 in neighbors1 and vert1 in neighbors2:
            return True
        else:
            return False


    def get_weight(self, vert1, vert2):
        """Takes two vertices and returns the weight value attached with the edge from vert1 to vert2. Returns multiple errors if either
        either of the vertex's don't exist, or if they're not connected
        WGraph, int, int -> int"""
        neighbors1 = WGraph.neighbors_with_weight(self, vert1)
        neighbors2 = WGraph.neighbors_with_weight(self, vert2)
        if neighbors1 == None:
            raise KeyError("Error, vertex1 does not exist within this dictionary")
        elif neighbors2 == None:
            raise KeyError("Error, vertex2 does not exist within this dictionary")
        if vert2 in neighbors1:
            return neighbors1[vert2]
        else:
            raise KeyError("Error, vertex1 does not have a connection with vertex2")

    def shortest_path(self, vert1, vert2):
        """Takes two vertices and returns a list of the path between the vertices that has the lowest total weight. Raises an error
        if the path doesn't exist
        WGraph, int, int -> List of ints"""
        if vert1 == vert2:
            return [vert1]
        pathList = []
        pathList.append([vert1])
        to_check = Stack([[vert1]])
        #This makes pathList become a list of lists of numbers
        while not to_check.is_empty():
            currentPath = to_check.pop()
            for neighbor in self.neighbors(currentPath[-1]):
                if neighbor not in currentPath:
                    to_check.push(currentPath + [neighbor])
                    pathList.append(currentPath + [neighbor])
        #Gets rid of paths that don't start at vert1 and end at vert2
        finalPaths = []
        for li in pathList:
            if li[0] == vert1 and li[-1] == vert2:
                finalPaths.append(li)
        lowestTotal = []
        for v in finalPaths:
            temp = 0
            for index in range(len(v)):
                if index != len(v) -1 :
                    temp += self.get_weight(v[index], v[index+1])
            lowestTotal.append(temp)
        lowest = 9999999
        for i in range(len(lowestTotal)):
            if lowestTotal[i] < lowest:
                lowest = lowestTotal[i]
        for index in range(len(lowestTotal)):
            if lowestTotal[index] == lowest:
                return finalPaths[index]
        raise KeyError("Error: No path between " + str(vert1) + " and " + str(vert2))
            
            


#B
graph1 = WGraph({1:{2:2, 5:10}, 2:{1:5, 6:3}, 3:{4:1}, 4:{}, 5:{6:2}, 6:{5:2, 7:4}, 7:{2:7}, 8:{3:1}})
