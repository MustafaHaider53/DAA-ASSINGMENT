class Graph:
    def __init__(self):
        self.edges = []  # List to store edges

    def add_edge(self, u, v, w=None):
        if w is None:
            self.edges.append((u, v))
        else:
            self.edges.append((u, v, w))

    def print_edges(self):
        for edge in self.edges:
            print( " -->" , edge )

    def has_edge(self, u, v):
        for edge in self.edges:
            if len(edge) == 2 and (edge == (u, v) or edge == (v, u)):
                return True
            elif len(edge) == 3 and ((edge[0], edge[1]) == (u, v) or (edge[1], edge[0]) == (u, v)):
                return True
        return False

    def vertexNeighbors(self, u):
        nbrs = []
        for edge in self.edges:
            if len(edge) == 2:
                if edge[0] == u:
                    nbrs.append(edge[1])
                elif edge[1] == u:
                    nbrs.append(edge[0])
            elif len(edge) == 3:
                if edge[0] == u:
                    nbrs.append((edge[1], edge[2]))
                elif edge[1] == u:
                    nbrs.append((edge[0], edge[2]))
        return nbrs

# Function to create a complete graph with n vertices
def create_complete_graph(n):
    graph = Graph()
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            graph.add_edge(i ,j)
    return graph

# For 4 vertices
complete_graph = create_complete_graph(4)

print("Edge list representation of the complete graph with 4 vertices:")
complete_graph.print_edges()
