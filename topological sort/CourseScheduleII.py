from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        q = deque([])
        outgoing = defaultdict(set)
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            outgoing[pre].add(course)
            in_degree[course] += 1
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            order.append(course)

            for neighbour in outgoing[course]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    q.append(neighbour)
        
        if len(order) != numCourses:
            return []
        
        return order

# Tests
sol = Solution()
# Testcase 1: numCourses = 2, prerequisites = [[1,0]]
print(sol.findOrder(2, [[1,0]]) == [0,1])
# Testcase 2: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,2,1,3] or sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,1,2,3]) 
# Testcase 3: numCourses = 1, prerequisites = []
print(sol.findOrder(1, []) == [0])
        