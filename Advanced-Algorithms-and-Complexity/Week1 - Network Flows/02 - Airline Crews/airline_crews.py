# python3
import queue


class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        busy_right = [False] * m

        def bfs():
            '''
            's' -> Source
            'a' -> Airline
            'c' -> Crew
            't' -> Sink
            '''
            q = queue.Queue()
            q.put(('s', None))
            path = []
            parents = {}
            visited_nodes = set()
            visited_nodes.add(('s', None))
            while not q.empty():
                currNode = q.get()
                if currNode[0] == 's':
                    for i in range(n):
                        if matching[i] == -1:
                            visited_nodes.add(('a', i))
                            parents[('a', i)] = ('s', None)
                            q.put(('a', i))
                elif currNode[0] == 'a':
                    i = currNode[1]
                    for j in range(m):
                        if adj_matrix[i][j] == 1 and matching[i] != j and ('c', j) not in visited_nodes:
                            visited_nodes.add(('c', j))
                            parents[('c', j)] = currNode
                            q.put(('c', j))
                elif currNode[0] == 'c':
                    j = currNode[1]
                    if not busy_right[j]:
                        # Here, we have successfully found a path.
                        # Now, we are going to retrace it.
                        prevNode = currNode
                        currNode = ('t', j)
                        while True:
                            path.insert(0, (prevNode, currNode))
                            if prevNode[0] == 's':
                                break
                            currNode = prevNode
                            prevNode = parents[currNode]
                        for edge in path:
                            if edge[0][0] == 'a':
                                matching[edge[0][1]] = edge[1][1]
                            elif edge[0][0] == 'c' and edge[1][0] == 't':
                                busy_right[edge[1][1]] = True
                        return True
                    else:
                        for i in range(n):
                            if j == matching[i] and ('a', i) not in visited_nodes:
                                visited_nodes.add(('a', i))
                                parents[('a', i)] = currNode
                                q.put(('a', i))
                # Sink is never being put into the queue.
                # No need to consider that particular case.
            return False
        while bfs():
            continue
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
