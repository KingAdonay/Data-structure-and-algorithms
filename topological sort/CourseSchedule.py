from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        outgoing = defaultdict(set)
        q = deque([])
        order = []
        
        # count incoming degrees for each course
        for course, pre in prerequisites:
            outgoing[pre].add(course)
            in_degree[course] += 1
        
        # add safe nodes to queue for exploration
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        # explore and remove dependecy, repeat
        while q:
            course = q.popleft()
            order.append(course)
            
            for neighbour in outgoing[course]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    q.append(neighbour)
        
       
        return len(order) == numCourses

# Tests
sol = Solution()
# Testcase 1: numCourses = 2, prerequisites = [[1,0]]
print(sol.canFinish(2, [[1,0]]) == True)
# Testcase 2: numCourses = 2, prerequisites = [[1,0],[0,1]] 
print(sol.canFinish(2, [[1,0],[0,1]]) == False)
# Testcase 3: numCourses = 20, prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]] 
print(sol.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]) == False)