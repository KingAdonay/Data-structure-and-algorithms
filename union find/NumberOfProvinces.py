from typing import List

'''
547. Number of Provinces

Group the cities into provices based on the values in the isConnected matrix using union find by tracking parents,
and count the number of parents with negative wights at the end. That indicates the head nodes (provinces).

Time Complexity: O(n^2) due to the nested loop to iterate through the isConnected matrix.
Space Complexity: O(n) for the union find data structure to track the provinces.
'''

class Helper:
    def __init__(self, n: int):
        self.n = n
        self.provinces = [-1] * n
    
    def find(self, node: int) -> int:
        parent = self.provinces[node]
        if parent < 0:
            return node, parent
        
        while self.provinces[parent] >= 0:
            parent = self.provinces[parent]
        
        self.provinces[node] = parent # Path compression
        
        return parent, self.provinces[parent]
    
    def union(self, node1, node2):
        parent1, weight1 = self.find(node1)
        parent2, weight2 = self.find(node2)

        if parent1 == parent2:
            return

        if weight1 <= weight2:
            self.provinces[node2] = parent1
            self.provinces[parent2] = parent1
            self.provinces[parent1] += weight2
        else:
            self.provinces[node1] = parent2
            self.provinces[parent1] = parent2
            self.provinces[parent2] += weight1
            
    
    def get_unique_provinces_count(self) -> int:
        res = 0
        for i in range(self.n):
            if (self.provinces[i] < 0):
                res += 1
        return res


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        helper = Helper(n)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    helper.union(i, j)
        
        return helper.get_unique_provinces_count()

# Tescases:
s = Solution()
print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2) # 2
print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3) # 3  
print(s.findCircleNum([[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]) == 3) # 3  
