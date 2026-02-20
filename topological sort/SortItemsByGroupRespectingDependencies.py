from typing import List
from collections import defaultdict, deque

'''
    1203. Sort Items by Groups Respecting Dependencies
    
    Intuition:
    We need to sort items based on their dependencies while also respecting the grouping of items.
    We need to perform a topological sort on both the items and the groups. The items within the same group should be sorted together,
    and the groups themselves should be sorted based on their dependencies.
    
    Approach:
    1. Group the ungrouped items by assigning them to a new group.
    2. Create a graph representation for both items and groups using adjacency lists and in-degree counts.
    3. Perform a topological sort on the items to get their order.
    4. Perform a topological sort on the groups to get their order.
    5. Group the items based on their group and concatenate them according to the group order.
    6. If the final sorted list of items does not contain all items, return an empty list, indicating that it's not possible to sort due to a cycle.
    
    Time complexity: O(n + e) where n is the number of items and e is the number of dependencies
    Space complexity: O(n + e) for the graph representation and in-degree tracking
'''

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        g_adj = defaultdict(set)
        g_in_degree = defaultdict(int)

        # Group the ungrouped items so that they won't be assumed as a single group (-1)
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = m
                m += 1

        for i, items in enumerate(beforeItems):
            for item in items:
                if group[item] != group[i] and group[i] not in g_adj[group[item]]:
                    g_in_degree[group[i]] += 1
                    g_adj[group[item]].add(group[i])
                in_degree[i] += 1
                adj[item].append(i)

        # Find topological order of items
        q = deque([])
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for nei in adj[cur]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        # Find topological order of groups
        q = deque([])
        for key in range(-1, m):
            if g_in_degree[key] == 0:
                q.append(key)

        g_order = []
        while q:
            cur = q.popleft()
            g_order.append(cur)
            for g in g_adj[cur]:
                g_in_degree[g] -= 1
                if g_in_degree[g] == 0:
                    q.append(g)
        
        # Group items and concatinate them based on the group ordering
        group_item = defaultdict(list)
        for num in res:
            group_item[group[num]].append(num)
        
        ans = []
        for g in g_order:
            ans += group_item[g]
        
        if len(ans) != n:
            return []

        return ans
        
# Tests
sol = Solution()
# Testcase 1:
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
print(sol.sortItems(n, m, group, beforeItems) == [6,3,4,5,2,0,7,1])
# Testcase 2:
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
print(sol.sortItems(n, m, group, beforeItems) == [])
# Testcase 3:
n = 3
m = 1
group = [-1,0,-1]
beforeItems = [[],[0],[1]]
print(sol.sortItems(n, m, group, beforeItems) == [0,1,2])