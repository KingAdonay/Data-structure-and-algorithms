import collections
from typing import List

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