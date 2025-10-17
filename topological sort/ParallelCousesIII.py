from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        '''
        Approach the problem as a tolopological sort using kahn's algorithm,
        whenever we get a safe node, the time it takes to complete that course is
        the time it took the previous node plus current course time
        and we compare this time with the max time of the queue, and take the max,
        since we can start courses simultinuously, max time will be the amount of 
        time needed to finish the course.

        track dependent course time so that 
        for a -> b -> c, time[c] is time[c] + time[b] + time[a] 

        and for a -> b and d -> b, time [b] is max(time[a], time[d]) + time[b]
        '''
        course_max = [0] * (n + 1)
        in_degree = [0] * (n + 1)
        adj = defaultdict(set)
        queue = deque([])
        max_time = 0

        for prev, next in relations:
            in_degree[next] += 1
            adj[prev].add(next)
        
        for course in range(1, n+1):
            if in_degree[course] == 0:
                max_time = max(max_time, time[course-1])
                course_max[course] = time[course-1]
                queue.append(course)
        
        while queue:
            prev = queue.popleft()
            for next in adj[prev]:
                in_degree[next] -= 1
                course_time = time[next-1] + course_max[prev] 
                course_max[next] = max(course_max[next], course_time)
                if in_degree[next] == 0:
                    max_time = max(max_time, course_max[next])
                    queue.append(next)
        
        return max_time


# Test cases:
solution = Solution()
print(solution.minimumTime(3, [[1,3],[2,3]], [3,2,5]) == 8)  # Output: 8
print(solution.minimumTime(5, [[1,5],[2,5],[3,5],[3,4],[4,5]], [1,2,3,4,5]) == 12)  # Output: 12
print(solution.minimumTime(3, [[1,2],[2,3]], [1,2,3]) == 6)  # Output: 6