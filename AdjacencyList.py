from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since the graph is undirected
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"Vertex {vertex}: ", end="")
            for neighbor in self.graph[vertex]:
                print(f"{neighbor} --> ", end="")
            print()

# Create a graph instance
g = Graph()

# Add edges to create a fully connected graph with 4 vertices 
vertices = [0, 1, 2, 3]
for i in range(len(vertices)):
    for j in range(i + 1, len(vertices)):
        g.add_edge(vertices[i], vertices[j])

# Print the adjacency list representation of the graph
g.print_graph()
