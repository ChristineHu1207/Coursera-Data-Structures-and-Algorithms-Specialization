# python3
import queue


class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for i in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def min_charts(self, stock_data):
        # Replace this incorrect greedy algorithm with an
        # algorithm that correctly finds the minimum number
        # of charts on which we can put all the stock data
        # without intersections of graphs on one chart.
        n = len(stock_data)
        m = len(stock_data[0])
        adj_matrix = [[0 for i in range(n)] for j in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                if all(x < y for (x, y) in tuple(zip(stock_data[i], stock_data[j]))):
                    adj_matrix[i][j] = 1
        # Now, we can follow the same procedure as the previous question.
        # The logic that has been used is that for two stock graphs to exist in the same plane without intersecting,
        # the lines must never touch each other --> one line is always greater than the other.
        # If we have such a matrix filled, then we can use the same principle as before to divide them into maximal
        # bipartite graphs.

        # The count of nodes that cannot be put in any other graph will have -1 as its value in matching array finally.
        # So, the count of such values is the required answer.

        # Amazing question. Amazing concepts and an elegant solution. :)
        matching = [-1] * n
        busy_right = [False] * n

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
                    for j in range(n):
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
        charts = 0
        for i in matching:
            if i == -1:
                charts += 1
        return charts

    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)


if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
