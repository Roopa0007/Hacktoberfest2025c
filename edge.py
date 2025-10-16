from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []

    def bfs(self, src, dest):
        visited = {node: False for node in self.graph}
        parent = {node: -1 for node in self.graph}
        queue = deque([src])
        visited[src] = True

        while queue:
            u = queue.popleft()
            if u == dest:
                path = []
                while u != -1:
                    path.append(u)
                    u = parent[u]
                return path[::-1]
            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        return []

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

source = 2
dest = 3

path = g.bfs(source, dest)
if path:
    print("Shortest path:", path)
else:
    print("Path not found")
