from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = defaultdict(set)
        in_degree = [0] * n
        children = defaultdict(set)
        queue = deque([])
        ans = [[]] * n

        for fromm, to in edges:
            in_degree[to] += 1
            children[fromm].add(to)
        
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for child in children[node]:
                ancestors[child].update(ancestors[node])
                ancestors[child].add(node)
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)
        
        for i in range(n):
            ans[i] = sorted(list(ancestors[i]))
        
        return ans
    

# Tests
sol = Solution()
# Testcase 1: n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(sol.getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]) == [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]])
# Testcase 2: n = 5, edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(sol.getAncestors(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]) == [[],[0],[0,1],[0,1,2],[0,1,2,3]])
# Testcase 3: n = 3, edges = [[1,2],[1,0],[2,0]]
print(sol.getAncestors(3, [[1,2],[1,0],[2,0]]) == [[1,2],[],[1]])
# Testcase 4: n = 3, edges = []
print(sol.getAncestors(3, []) == [[],[],[]])