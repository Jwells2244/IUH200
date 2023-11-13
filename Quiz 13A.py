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
