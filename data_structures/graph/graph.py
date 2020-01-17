class UnweightedGraph:
    def __init__(self, g):
        self.graph = g

    def add_edge(self, vertex, neighbour):
        if vertex not in self.graph:
            self.graph[vertex] = [neighbour]
        else:
            self.graph[vertex].append(neighbour)

    def print(self):
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                print(('{}----{}').format(vertex, neighbour))

    def find_path(self, start, end, path=[]):
        path += [start]

        if start == end:
            return path

        for vertex in self.graph[start]:
            if vertex not in path:
                new_path = self.find_path(vertex, end, path)
                if new_path:
                    return new_path
                return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph:
            return []

        paths = []
        for vertex in self.graph[start]:
            if vertex not in path:
                newpaths = self.find_all_paths(vertex, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def BFS(self, start):
        visited = {vertex: False for vertex in self.graph}

        queue = [start]
        visited[start] = True

        while queue:
            vertex = queue.pop(0)
            print(vertex, end='->')

            for neighbour in self.graph[vertex]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True
        print('Done')

    def DFS(self, start):
        def DFS_helper(vertex, visited):
            visited[vertex] = True
            print(vertex, end='->')

            for neighbour in self.graph[vertex]:
                if not visited[neighbour]:
                    self.DFS_helper(neighbour, visited)

        visited = {vertex: False for vertex in self.graph}

        DFS_helper(start, visited)
        print('Done')

    def topological_sort(self, node):
        def topological_sort_helper(node):
            for neighbour in self.graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    topological_sort_helper(neighbour)
            res.insert(0, neighbour)

        res = []
        visited = {vertex: False for vertex in self.graph}
        topological_sort_helper(node)
        return res


g = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'G'],
         'C': ['A', 'E', 'F'],
         'D': ['A', 'F', 'H'],
         'E': ['B', 'C', 'G', 'I'],
         'F': ['C', 'D', 'I', 'H'],
         'G': ['B', 'E', 'I'],
         'H': ['D', 'F', 'I'],
         'I': ['E', 'F', 'G', 'H']}

graph = UnweightedGraph(g)
# print(graph.find_path('E', 'A'))
# graph.print()
# graph.BFS('A')
# graph.DFS('A')
# print(graph.find_all_paths('A', 'G'))
print(graph.topological_sort('C'))
