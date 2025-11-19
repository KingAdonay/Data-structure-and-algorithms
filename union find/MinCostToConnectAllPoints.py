from typing import List

'''
LeetCode 1584. Min Cost to Connect All Points

Find the costs of the edges betweek all points, sort them and use union find to connect the points with minimum cost. This algorithm is
similar to Kruskal's algorithm for finding the Minimum Spanning Tree (MST) of a graph.

N is the number of points and E is the number of edges between the points. To find the costs of all edges, we need to iterate through 
all pairs of points which takes O(N^2) time.

Time complexity: O(N^2 * α(N)) where α is the Inverse Ackermann function, which is very slow growing and for all practical purposes 
can be considered a constant. Thus, the time complexity can be approximated to O(N^2).
Space complexity: O(N^2) to store all the edges between the points.
'''

class DSU:
    def __init__(self, sz: int):
        self.parents = [-1] * sz
        self.costs = [0] * sz
    
    def find(self, p: int):
        parent = self.parents[p]
        if parent < 0:
            return p, parent
        
        parent, size = self.find(parent)
        self.parents[p] = parent
        return parent, size

    def union(self, p1: int, p2:int, cost: int) -> int:
        parent1, size1 = self.find(p1)
        parent2, size2 = self.find(p2)
        new_cost = cost

        if parent1 == parent2:
            return abs(size1), self.costs[p1]
        
        new_weight = size1 + size2
        if size1 <= size2:
            self.parents[parent2] = parent1
            self.parents[parent1] = new_weight
            self.costs[parent1] += cost +  self.costs[parent2]
            new_cost = self.costs[parent1]
        else:
            self.parents[parent1] = parent2
            self.parents[parent2] = new_weight
            self.costs[parent2] += cost + self.costs[parent1]
            new_cost = self.costs[parent2]
        
        return abs(new_weight), new_cost
        

class Solution:
    def manhattan_distance(self, point1:int, point2:int) -> int:
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []
        adjecents = set()

        for i in range(n):
            for j in range(n):
                edge = sorted([i, j])
                key = (edge[0], edge[1])
                if i != j and key not in adjecents:
                    cost = self.manhattan_distance(points[i], points[j])
                    adjecents.add(key)
                    edges.append((cost, i, j))
        

        edges.sort(key=lambda x: x[0])

        for cost, p1, p2 in edges:
            size, cost = dsu.union(p1, p2, cost)
            if size == n:
                return cost
        
        return 0

