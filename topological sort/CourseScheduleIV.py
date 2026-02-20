import collections
from typing import List

'''
    1462. Course Schedule IV
    Intuition:
    We need to determine if one course is a prerequisite of another course based on the given prerequisites.
    We need to find all the ancestors (prerequisites) for each course and then check if the queried prerequisite is in the set of ancestors for the course.
    
    Approach:
    1. Create a graph representation of the courses and their prerequisites using an adjacency list and an in-degree count.
    2. Perform a topological sort using a queue to find the ancestors for each course.
    3. For each query, check if the prerequisite is in the set of ancestors for the course and return the result.
    
    Time complexity: O(n + e + q) where n is the number of courses, e is the number of prerequisites, and q is the number of queries
    Space complexity: O(n + e) for the graph representation and ancestor tracking
    
'''

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ancestors = collections.defaultdict(set)
        adj = collections.defaultdict(set)
        in_degree = [0] * numCourses
        queue = collections.deque([])

        for pre, course in prerequisites:
            in_degree[course] += 1
            adj[pre].add(course)
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            for node in adj[course]:
                ancestors[node].update(ancestors[course])
                ancestors[node].add(course)
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    queue.append(node)
        ans = [False] * len(queries)
        for i, query in enumerate(queries):
            pre, course = query
            if pre in ancestors[course]:
                ans[i] = True
        
        return ans
    
# Test cases:
solution = Solution()
print(solution.checkIfPrerequisite(2, [[1,0]], [[0,1],[1,0]]))  # Output: [False, True]
print(solution.checkIfPrerequisite(2, [], [[1,0],[0,1]]))  # Output: [False, False]
print(solution.checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))  # Output: [True, True]    