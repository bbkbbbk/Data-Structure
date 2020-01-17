from decimal import Decimal


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for c in range(vertices)] for r in range(vertices)]

    def print(self, dist):
        for node in range(self.vertices):
            print("{}:{} ".format(node + 1, dist[node]), end='')
        print()

    def min_distance(self, dist, seen):
        small = Decimal("inf")
        for v in range(self.vertices):
            if dist[v] < small and seen[v] == False:
                small = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        # set the provisional dist of all node to infinity
        dist = [Decimal("inf")] * self.vertices

        # set the provisional dist of src node = 0
        dist[src] = 0

        # set all not to not seen
        seen_node = [False] * self.vertices

        for _ in range(self.vertices):
            # set cur node to the min node in the entire graph
            u = self.min_distance(dist, seen_node)

            # bc have seen this node
            seen_node[u] = True
            for v in range(self.vertices):
                # if the val < neighbor's cur provisional dist
                # update the provisional dist of each cur node's neighbors to be dist from cur node
                # to src node + the edge length from cur node
                if self.graph[u][v] > 0 and not seen_node[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]  # update provisional distance

        self.print(dist)


g = Graph(9)
g.graph = [[0, 1, 4, 3, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 5, 0, 10, 0, 0],
           [4, 0, 0, 0, 5, 0, 10, 0, 0],
           [3, 0, 0, 0, 0, 3, 0, 5, 0],
           [0, 5, 6, 0, 0, 0, 6, 0, 8],
           [0, 0, 3, 3, 0, 0, 0, 2, 4],
           [0, 10, 0, 0, 6, 0, 0, 0, 3],
           [0, 0, 0, 5, 0, 2, 0, 0, 1],
           [0, 0, 0, 0, 8, 4, 3, 1, 0]]
for i in range(g.vertices):
    print(i + 1, ": ", end="")
    g.dijkstra(i)
