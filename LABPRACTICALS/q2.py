
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list:
            self.adj_list[vertex1] = []
        if vertex2 not in self.adj_list:
            self.adj_list[vertex2] = []
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
