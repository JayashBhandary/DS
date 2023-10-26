class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                self.graph[v] = [neighbor for neighbor in self.graph[v] if neighbor != vertex]

    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            self.graph[from_vertex] = [neighbor for neighbor in self.graph[from_vertex] if neighbor != to_vertex]

    def has_vertex(self, vertex):
        return vertex in self.graph

    def has_edge(self, from_vertex, to_vertex):
        return from_vertex in self.graph and to_vertex in self.graph[from_vertex]

    def display_adjacency_list(self):
        for vertex in self.graph:
            print(f"{vertex} -> {', '.join(map(str, self.graph[vertex]))}")

if __name__ == "__main__":
    my_graph = Graph()

    my_graph.add_vertex(1)
    my_graph.add_vertex(2)
    my_graph.add_vertex(3)
    my_graph.add_vertex(4)

    my_graph.add_edge(1, 2)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(2, 3)
    my_graph.add_edge(3, 1)
    my_graph.add_edge(3, 4)
    my_graph.add_edge(4, 4)

    print("Adjacency List of the Graph:")
    my_graph.display_adjacency_list()

    print("Removing vertex 2 and edge (1, 3)...")
    my_graph.remove_vertex(2)
    my_graph.remove_edge(1, 3)

    print("Adjacency List after removal:")
    my_graph.display_adjacency_list()
