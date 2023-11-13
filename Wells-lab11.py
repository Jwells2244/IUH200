#Lab 11

#A
class Graph:
    """A collection of vertices, called nodes, and a collection of undirected edges that tell us which vertices
    are connected to other vertices. When two vertices are directly connected by an edge, we say that they are
    adjacent to one another."""
    #Private Attributes:
    #dict: a dictionary
#B
    def __init__(self, vertices={}):
        """Initializes self with the given inputs, vertices and edges
        Graph, dict -> None"""
        self._dict = vertices
#C
    def __repr__(self):
        """Returns a string in the form Graph(dict)
        Graph -> String"""
        return "Graph("+repr(self._dict)+")"
#D
    def neighbors(self, vertex):
        """Takes the vertex and returns the set of the vertices that are adjacent to it
        Graph, int -> Set or None if the vertex does not exist"""
        if vertex in self._dict:
            return self._dict[vertex]
        else:
            return None
#E      
    def is_adjacent_to(self, vert1, vert2):
        """Takes two vertices, vert1 and vert2, and determines whether they are adjacent to each other in the graph
        Graph, int, int -> Boolean"""
        neighbors1 = Graph.neighbors(self, vert1)
        neighbors2 = Graph.neighbors(self, vert2)
        if vert2 in neighbors1 and vert1 in neighbors2:
            return True
        else:
            return False
#F
    def add_vertex(self, vertex):
        """Takes a vertex label, and adds it to dict, with a blank set of vertices attached, if it does not already exist
        Graph, int -> None"""
        test = Graph.neighbors(self, vertex)
        if test == None:
            self._dict[vertex] = set()

#G
    def add_edge(self, vert1, vert2):
        """Takes two vertices and adds an edge between them, if it does not already exist
        Graph, int, int -> None"""
        self._dict[vert1].add(vert2)
        self._dict[vert2].add(vert1)

#H

    def remove_vertex(self, vertex):
        """Takes a vertex and removes it from dict if it exists. If it doesn't exist, throws a BLANK error
        Graph, int -> None"""
        success = self._dict.pop(vertex, None)
        if success == None:
            raise KeyError("Error, vertex does not exist within this dictionary")
        for sett in self._dict:
            if vertex in self._dict[sett]:
                self._dict[sett].remove(vertex)
#I
    def remove_edge(self, vert1, vert2):
        """Takes two vertices and removes the edge between them. If it doesn't exist, throws a KeyError
        Graph, int, int -> None"""
        if Graph.is_adjacent_to(self, vert1, vert2):
            self._dict[vert1].remove(vert2)
            self._dict[vert2].remove(vert1)
        else:
            raise KeyError("Error, Key does not exist in dictionary")

    def are_connected(self, x, y):
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
            for neighbor in self.neighbors(curr_vert):
                if neighbor not in connected:
                    connected.add(neighbor)
                    to_check.push(connected)
        return False

graph1 = Graph({0:{1,2}, 1:{0,7}, 2:{0,3,4}, 3:{2,4}, 4:{2,3}, 5:{6}, 6:{5}, 7:{1,8}, 8:{7}})
        
    
        
