class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        depth = [1] * n
        q = deque([])
        
        max_cycle_len, open_table = 0, 0
        
        for per in range(n):
            indegree[favorite[per]] += 1
        
        for per in range(n):
            if indegree[per] == 0:
                q.append(per)
        
        while q:
            cur_per = q.popleft()
            next_per = favorite[cur_per]
            
            depth[next_per] = max(depth[next_per], depth[cur_per] + 1)
            
            indegree[next_per] -= 1
            if indegree[next_per] == 0:
                q.append(next_per)
        
        for per in range(n):
            if indegree[per] == 0: continue
            
            cycle_len = 0
            cur = per
            while indegree[cur] != 0:
                indegree[cur] = 0
                cycle_len += 1
                cur = favorite[cur]
            
            if cycle_len == 2:
                open_table += depth[per] + depth[favorite[per]]
            else:
                max_cycle_len = max(max_cycle_len, cycle_len)
        
        return max(max_cycle_len, open_table)
        

'''
examples:
[2,2,1,2] -> 3

[1,2,0] -> 3

[3,0,1,4,1] -> 4
'''