from typing import List

class Solution:
    # naive solution
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        ans = []
        tuples = []

        for i, p in enumerate(position):
            distance_to_target = target - p
            t = distance_to_target / speed[i]

            tuples.append((distance_to_target, t))
        
        tuples.sort()

        selected_distance = tuples[0][0]
        selected_time = tuples[0][1]
        count = 1
        i = 0
        while i in range(n):
            d, t = tuples[i]
            
            if t > selected_time:
                selected_time = t
                selected_distance = d
                count += 1
            else:
                selected_time = max(selected_time, t)

            i += 1

        return count
    
    def carFleetEfficient(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = zip(position, speed)
        position_time_list= [(p, (target - p) / s) for p, s in position_speed]

        position_time_list = sorted(position_time_list, key=lambda x:x[0], reverse=True)
        stack = []
        for _, t in position_time_list:
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)
    
# Tests
sol = Solution()
# Testcase 1: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3], expected = 3
# Testcase 2: target = 12, position = [10], speed = [2], expected = 1
# Testcase 3: target = 100, position = [0,2,4], speed = [4, 2, 1], expected = 1
# Testcase 4: target = 10, position = [0,4,2], speed = [2,1,3], expected = 1

print(3 == sol.carFleetEfficient(target=12, position=[10,8,0,5,3], speed = [2,4,1,1,3]))