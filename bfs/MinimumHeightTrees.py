from typing import List
from collections import defaultdict

'''
    310. Minimum Height Trees
    
    Intuition:
    The minimum height trees will be the ones with the centroids as roots. A tree can have one or two centroids. 
    We can find the centroids by repeatedly removing the leaves until we are left with one or two nodes.
    
    Approach:
    1. Create a graph representation of the tree using an adjacency list.
    2. Identify the initial leaves (nodes with only one connection).
    3. While there are more than 2 nodes in the graph:
        3.1 Remove the current leaves and update the graph.
        3.2 Identify new leaves after removal.
    4. The remaining nodes will be the centroids, which are the roots of the minimum height trees.
    
    Time complexity: O(n) where n is the number of nodes
    Space complexity: O(n) for the graph representation and leaf tracking
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        if n == 1:
            return [0]
        
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        leaves = [key for key, value in graph.items() if len(value) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                node = graph[leaf].pop()
                graph[node].remove(leaf)

                if len(graph[node]) == 1: new_leaves.append(node)
            leaves = new_leaves

        return leaves

# Tests
sol = Solution()
# Testcase 1:
n = 4
edges = [[1,0],[1,2],[1,3]]
print(sol.findMinHeightTrees(n, edges) == [1])
# Testcase 2:
n = 6
edges = [[0,3],[1,3],[2,3],[4,3],[5,4]]
print(sol.findMinHeightTrees(n, edges) == [3,4])
# Testcase 3:
n = 1
edges = []
print(sol.findMinHeightTrees(n, edges) == [0])
# Testcase 4:
n = 2
edges = [[0,1]]
print(sol.findMinHeightTrees(n, edges) == [0,1])