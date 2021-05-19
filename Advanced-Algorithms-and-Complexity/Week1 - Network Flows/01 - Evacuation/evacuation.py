# python3

import queue


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.


class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].capacity -= flow
        self.edges[id ^ 1].capacity += flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def bfs(graph, from_, to):
    if from_ == to:
        return True, [], 0
    path = []
    parent = [(None, None) for _ in range(graph.size())]
    distance = [float('inf') for _ in range(graph.size())]
    min_edge_in_path = float('inf')
    path_exists = False
    kyu = queue.Queue()
    kyu.put(from_)
    distance[from_] = 0
    while not kyu.empty():
        currNode = kyu.get()
        for id in graph.get_ids(currNode):
            currEdge = graph.get_edge(id)
            if distance[currEdge.v] == float('inf') and currEdge.capacity > 0:
                kyu.put(currEdge.v)
                distance[currEdge.v] = distance[currNode] + 1
                parent[currEdge.v] = (currNode, id)
                if currEdge.v == to:
                    while True:
                        path.insert(0, id)
                        curr_edge_capacity = graph.get_edge(id).capacity
                        min_edge_in_path = min(
                            min_edge_in_path, curr_edge_capacity)
                        if currNode == from_:
                            break
                        currNode, id = parent[currNode]
                    path_exists = True
                    return path_exists, path, min_edge_in_path
    return path_exists, path, min_edge_in_path


def max_flow(graph, from_, to):
    flow = 0
    # your code goes here
    while True:
        path_exists, path, min_capacity = bfs(graph, from_, to)
        if path_exists:
            for id in path:
                graph.add_flow(id, min_capacity)
        else:
            return flow
        flow += min_capacity
    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
