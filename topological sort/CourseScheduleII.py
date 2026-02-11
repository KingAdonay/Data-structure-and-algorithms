from typing import List
from collections import defaultdict, deque

'''
    210. Course Schedule II
    Intuition:
    We can use topological sorting to determine the order of courses to take based on their prerequisites.
    If there is a cycle in the graph, it means that it's impossible to complete all courses
    
    Approach:
    1. Create a graph representation of the courses and their prerequisites using an adjacency list.
    2. Calculate the in-degree (number of prerequisites) for each course.
    3. Use a queue to perform a breadth-first search (BFS) starting with courses that have an in-degree of 0 (no prerequisites).
    4. For each course taken, reduce the in-degree of its neighboring courses (courses that depend on it) by 1.
    5. If any neighboring course's in-degree becomes 0, add it to the queue.
    6. Keep track of the order of courses taken. If the number of courses taken is equal to numCourses, return the order. Otherwise, return an empty list. 
    
    Time complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
    Space complexity: O(V + E) for the graph representation and in-degree array
'''


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
        