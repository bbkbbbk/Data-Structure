INF = float('inf')

class WeightedGraph:
    class Edge:
        def __init__(self, start, end, cost):
            self.start = start
            self.end = end
            self.cost = cost

    def __init__(self, edges):
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data:', wrong_edges)

        self.edges = [self.Edge(*edge) for edge in edges]

    def vertices(self):
        return set(sum(([edge.start, edge.end] for edge in self.edges), []))

    def get_node_pair(self, x, y, both_ends=True):
        if both_ends:
            node_pairs = [[x, y], [y, x]]
        else:
            node_pairs = [[x, y]]
        return node_pairs

    def add_edge(self, x, y, cost=1, both_ends=True):
        node_pairs = self.get_node_pair(x, y, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                print('Edge {} {}already exists'.format(x, y))
                return
        self.edges.append(self.Edge(x, y, cost))
        if both_ends:
            self.edges.append(self.Edge(y, x, cost))

    def remove_edge(self, x, y, both_ends=True):
        node_pairs = self.get_node_pair(x, y, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def get_neighbour(self):
        neighbours = {vertex: set() for vertex in self.vertices()}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))
        return neighbours

    def dijkstra(self, source, dest):
        # 1. Mark all nodes unvisited and store them.
        # 2. Set the distance to zero for our initial node
        # and to infinity for other nodes.
        distances = {vertex: INF for vertex in self.vertices()}
        previous_vertices = {vertex: None for vertex in self.vertices()}
        distances[source] = 0
        vertices = self.vertices()

        while vertices:
            # 3. Select the unvisited node with the smallest distance,
            # it's current node now.
            current_vertex = min(vertices, key=lambda vertex: distances[vertex])

            # 6. Stop, if the smallest distance
            # among the unvisited nodes is infinity.
            if distances[current_vertex] == INF:
                break

            # 4. Find unvisited neighbors for the current node
            # and calculate their distances through the current node.
            neighbours = self.get_neighbour()
            for neighbour, cost in neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost

                # Compare the newly calculated distance to the assigned
                # and save the smaller one.
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

            # 5. Mark the current node as visited
            # and remove it from the unvisited set.
            vertices.remove(current_vertex)

        path, current_vertex = [], dest
        while previous_vertices[current_vertex] is not None:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.append(current_vertex)
        return path

    def distance_between_nodes(self, start, end):
        distance_between_nodes = 0
        path = self.dijkstra(start, end)

        for index in range(1, len(path)):
            for thing in self.edges:
                if thing.start == path[index] and thing.end == path[index - 1]:
                    distance_between_nodes += thing.cost
        return distance_between_nodes


g = ([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
      ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
      ("e", "f", 9)])

g = WeightedGraph(g)
print(g.dijkstra("a", "e"))
print(g.distance_between_nodes('a', 'e'))
