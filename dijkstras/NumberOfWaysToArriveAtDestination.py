from collections import defaultdict
import heapq
from typing import List

'''
1976. Number of Ways to Arrive at Destination

To find the minium time to reach a destination and the number of ways to reach the destination in that cost,
we can use Dijkstra's algorithm.

Time complexity: O(N + ElogE), where N is the number of nodes and E is the number of edges.
Space complexity: O(N + E), where N is the number of nodes and E is the number of edges.
'''


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        adj = defaultdict(list)

        for x, y, t in roads:
            adj[x].append((y, t))
            adj[y].append((x, t))
        
        shortest_time_count_list = [[float('inf'), 0] for _ in range(n)]
        shortest_time_count_list[0][0] = 0
        shortest_time_count_list[0][1] = 1

        min_heap = [(0, 0)]
        while min_heap:
            cur_time, cur_node = heapq.heappop(min_heap)
            if cur_time > shortest_time_count_list[cur_node][0]:
                continue

            for neighbour, time in adj[cur_node]:
                new_time = shortest_time_count_list[cur_node][0] + time
                
                if new_time == shortest_time_count_list[neighbour][0]:
                    shortest_time_count_list[neighbour][1] = (shortest_time_count_list[neighbour][1] + shortest_time_count_list[cur_node][1]) % MOD
                elif new_time < shortest_time_count_list[neighbour][0]:
                    shortest_time_count_list[neighbour][0] = new_time
                    shortest_time_count_list[neighbour][1] = shortest_time_count_list[cur_node][1]
                    heapq.heappush(min_heap, (shortest_time_count_list[neighbour][0], neighbour))
            
       
        return shortest_time_count_list[-1][1]
            
# Testcases
# Testcase 1: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]] -> 4
# Testcase 2: n = 2, roads = [[1,0,10]] -> 1