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


class Graph:
    """An undirected graph."""
    
    def __init__(self, graphdict = None):
        """Initializes self with the given dictionary (vertices as keys,
        sets of neighboring vertices as values) or with an empty graph.
        Vertice are usually ints, but don't have to be).
        Graph[, dict(vertex:set-of-vertices)] -> None"""
        if graphdict==None:
            self._graphdict = dict()
        else:
            self._graphdict = graphdict

    def get_graphdict(self):
        """Returns the graph dictionary (vertices as keys,
        sets of neighboring vertices as values).
        Graph -> dict(vertex:set-of-vertices)"""
        return self._graphdict
    
    def __repr__(self):
        """Returns a string of the form Graph(graphdict)
        Graph -> str"""
        return "Graph(" + repr(self.get_graphdict()) + ")"

    def add_vertex(self, x):
        """Adds the given vertex to the Graph self.
        Graph, vertex -> None"""
        if x in self.get_graphdict():
            raise ValueError("Vertex already in graph.")
        else:
            self._graphdict[x] = set()

    def add_edge(self, x, y):
        """Adds an edge between the given vertices to the Graph self.
        Graph, vertex, vertex -> None"""
        if x not in self.get_graphdict():
            raise KeyError("No such vertex: " + repr(x))
        elif y not in self.get_graphdict():
            raise KeyError("No such vertex: " + repr(y))
        else:
            self._graphdict[x].add(y)
            self._graphdict[y].add(x)

    def neighbors_of(self, x):
        """Returns a set of neighbors of the vertex x.
        Graph, vertex -> set-of-vertices"""
        if x not in self.get_graphdict():
            raise KeyError("No such vertex: " + repr(x))
        else:
            return self._graphdict[x]

    def are_adjacent(self, x, y):
        """Determines whether x and y are neighbors.
        Graph, vertex, vertex -> bool"""
        if x not in self.get_graphdict():
            raise KeyError("No such vertex: " + repr(x))
        elif y not in self.get_graphdict():
            raise KeyError("No such vertex: " + repr(y))
        else:
            return y in self.neighbors_of(x)

        


    def are_connected_DFS(self, x, y):
            """Determines whether there is a path from x to y
            Graph, vertex, vertex -> Bool"""

            #if first to-check is a queue, then what we're doing is a breadth first search

            #if first to check is a stack, then what we're doing is a depth first search

            connected = {x}
            to_check = Stack([x])

            while not to_check.is_empty():
                if y in connected:
                    return True
                curr_vert = to_check.pop()
                print("Checking " + str(curr_vert) + " ... ")
                for neighbor in self.neighbors_of(curr_vert):
                    if neighbor not in connected:
                        connected.add(neighbor)
                        to_check.push(neighbor)
            return False
        
    #Quiz 13A
    def are_connected_BFS(self, x, y):
        """Determines whether there is a path from x to y
        Graph, vertex, vertex -> Bool"""
        connected = {x}
        to_check = Queue([x])

        while not to_check.is_empty():
            if y in connected:
                return True
            curr_vert = to_check.dequeue()
            print("Checking " + str(curr_vert) + " ... ")
            for neighbor in self.neighbors_of(curr_vert):
                if neighbor not in connected:
                    connected.add(neighbor)
                    to_check.enqueue(neighbor)
        return False
graph1 = Graph({0:{1,2}, 1:{0,7}, 2:{0,3,4}, 3:{2,4}, 4:{2,3}, 5:{6}, 6:{5}, 7:{1,8}, 8:{7}})


                
        
