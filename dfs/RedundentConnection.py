from typing import List
from collections import defaultdict

'''
    684. Redundant Connection
    
    Intuition:
    We need to find the edge that creates a cycle in the graph. We can use depth-first search (DFS) to detect cycles in the graph.
    When we find a node that has already been visited during our DFS, it means we have found a cycle. We can keep track of the edges 
    that are part of the cycle and return the last edge that was added to the graph which is part of the cycle.
    
    Approach:
    1. Create a graph representation of the edges using an adjacency list.
    2. Use a DFS helper function to traverse the graph and detect cycles. Keep track of visited nodes and the edges that are part of the cycle.
    3. After the DFS, iterate through the edges in reverse order and return the first edge that is part of the cycle.
    
    Time complexity: O(n * m) where n is the number of edges, m is the number of nodes in the graph (in the worst case, we might visit all nodes for each edge)
    Space complexity: O(n + m)
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        ans = set()

        def helper(start, prev):
            for node in adj[start]:
                if node == prev:
                    continue
                if node in visited:
                    ans.add((start, node))
                    return
                visited.add(node)
                helper(node, start)
                visited.remove(node)
        
        for start in adj.keys():
            visited.add(start)
            helper(start, start)
            visited.remove(start)
        
        for i in range(len(edges) - 1, -1, -1):
            if (edges[i][0], edges[i][1]) in ans or (edges[i][1], edges[i][0]) in ans:
                return edges[i]
        
        return []


# Tests
sol = Solution()
# Testcase 1: edges = [[1,2],[1,3],[2,3]]
print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]) == [2,3])
# Testcase 2: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1,4])