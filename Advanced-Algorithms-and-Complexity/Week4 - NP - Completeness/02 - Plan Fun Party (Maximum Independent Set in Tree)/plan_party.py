#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent, weights):
    # for child in tree[vertex].children:
    #     if child != parent:
    #         dfs(tree, child, vertex)

    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.
    
    if weights[vertex] == -1:
        if vertex != 0 and len(tree[vertex].children) == 1:
            # This is the case when the vertex is a leaf node. Only parent node has an edge to it.
            weights[vertex] = tree[vertex].weight
        else:
            weight1 = tree[vertex].weight
            # This var calculates the total max weight if this node is to be included.
            weight0 = 0            
            # This var calculates the total max weight if this node is not included.
            for v in tree[vertex].children:
                if v != parent:
                    weight0 += dfs(tree, v, vertex, weights)
                    for w in tree[v].children:
                        if w != vertex:
                            weight1 += dfs(tree, w, v, weights)
            weights[vertex] = max(weight0, weight1)
    
    return weights[vertex]
        


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    weights = [-1 for _ in range(size)]
    maxWeight = dfs(tree, 0, -1, weights)
    # You must decide what to return.
    return maxWeight


def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
