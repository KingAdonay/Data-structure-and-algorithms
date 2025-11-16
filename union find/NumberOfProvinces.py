from typing import List

'''
547. Number of Provinces

Group the cities into provices based on the values in the isConnected matrix using union find by tracking parents,
and count the number of parents with negative wights at the end. That indicates the head nodes (provinces).
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = [-1] * n

        def find(idx: int) -> int:
            if (parents[idx] < 0):
                return idx, parents[idx]
            return find(parents[idx])
        
        def union(city1: int, city2: int) -> None:
            parent1, weight1 = find(city1)
            parent2, weight2 = find(city2)

            if parent1 == parent2:
                return

            if weight1 <= weight2:
                parents[city2] = parent1
                parents[parent1] += weight2
                parents[parent2] = parent1
            else:
                parents[city1] = parent2
                parents[parent2] += weight1
                parents[parent1] = parent2
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)

        res = 0
        for i in range(n):
            if (parents[i] < 0):
                res += 1
        
        return res
    
# Tescases:
s = Solution()
print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2) # 2
print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3) # 3  
print(s.findCircleNum([[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]) == 3) # 3  
