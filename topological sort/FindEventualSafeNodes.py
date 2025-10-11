from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        ans = [False] * len(graph)

        def dfs(v):
            if v >= len(graph):
                return True
            
            if v in visited:
                return ans[v]
            
            res = True
            nodes = graph[v]
            visited.add(v)
            for node in nodes:
                res = res and dfs(node)
            
            ans[v] = res
            
            return res
        
        for i in range(len(graph)):
            if i not in visited:
                dfs(i)
            
        result = []
        for i in range(len(graph)):
            if ans[i]:
                result.append(i)

        return result

# Tests
sol = Solution()
# Testcase 1: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]) == [2,4,5,6])
# Testcase 2: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(sol.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]) == [4])