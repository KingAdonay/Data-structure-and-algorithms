from collections import Counter, deque
from typing import List

'''
The idea behind my solution is to process the most frequent task on every iteration, and after processing a single task,
making sure that our condition (n number of intervals before processing the same task) is met by processing other tasks or staying idle
before going to next iteration.

In order to achieve this we can use the Counter class to calculate the original frequency of each task in the tasks list, and
use the sorted function to get a list of the tasks (keys of counts) sorted based on the frequency of tasks in the count object.

For example, for data input ["A", "A", "A", "C", "C", "B", "B", "B", "D"], n = 2
counter = { "A": 3, "C":2, "B": 3, "D": 1 }
freq = ["A", "B", "C", "D"]

This sorting step will be done on every iteration and changed into a double ended queue to get a constant pop time from the left.
The sorting will happen on a maximum of 26 items so it is very fast.

Iteration steps:
1, we check if count of the most frequent task (freq[0]) in counter object is GREATER than 0:
    1.1 if it is greater than zero:
        1.1.1. we would first add the task in the answers (ans) list and decrement the count of the task in the counter object.
        
            Eg. counter object on first iteration with the above example will be { "A": 2, "C":2, "B": 3, "D": 1 }
            ans = ["A"]
            freq= ["A", "B", "C", "D"]

        1.1.2. After this we make sure our condition is met (n number of intervals) before executing the next task, I had to make sure,
            because the next frequent task could be the same task we just processed.

            So if the processed task have a count more than zero at this stage, it would loop over the frequency array until n intervals are achieved
            or until we loop over the whole frequncy array (26 max).

            This looping process uses two pointer method to process the most frequence one if count is more than zero or the less frequent one, and it
            always starts from the next frequent task.

            Eg. counter = { "A": 2, "C":1, "B": 2, "D": 0 }
            ans = ["A", "B", "C", "D"]
            freq= ["A", "B", "C", "D"]


        1.1.3 If the n intervals requirement is not fulfilled after loop terminates, that means we don't have other processable tasks so we would
        put in "idle" in ans until the condition is met.

        
2. if count of the most frequent task (freq[0]) IS zero:
    we would remove the task from the freq queue and sort the frequency queue based on the current state of the counter object and continue.
    Eg. if count of A is zero, we would remove A from the queue, [A, B, C, D] -> [B, C, D]

3. sort the frequency queue (freq) using the latest count object, so that it would have the most frequent task at the head of the queue.

Time complexity: O(n * m) Space: O(n), m = 26

I think it has approximately linear time because m is 26.

Full example, inputs: ["A", "A", "A", "C", "C", "B", "B", "B", "D"], n = 3
counter = {'A': 3, 'B': 3, 'C': 2, 'D': 1}
freq = ['A', 'B', 'C', 'D']
ans = []

Iterations:
1. freq = ['A', 'B', 'C', 'D']  counter = {'A': 2, 'B': 2, 'C': 1, 'D': 0} ans = ['A', 'B', 'C', 'D']
2. freq = ['A', 'B', 'C', 'D']  counter = {'A': 1, 'B': 1, 'C': 0, 'D': 0} ans = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'idle']
3. freq = ['B', 'C', 'D']  counter = {'B': 1, 'A': 0, 'C': 0, 'D': 0} ans = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'idle', 'A']
4. freq = ['C', 'D']  counter = {'A': 0, 'C': 0, 'B': 0, 'D': 0} ans = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'idle', 'A', 'B']
5. freq = ['D']  counter = {'A': 0, 'C': 0, 'B': 0, 'D': 0} ans = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'idle', 'A', 'B']
6. freq = []  counter = {'A': 0, 'C': 0, 'B': 0, 'D': 0} ans = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'idle', 'A', 'B']

'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        freq = deque(sorted(counter, key=lambda x:counter[x], reverse=True))
        
        ans = []
        i = 0
        while freq:
            if counter[freq[0]] > 0:
                ans.append(freq[0])
                counter[freq[0]] -= 1
                
                left = 1
                right = len(freq) - 1
                idle_count = n
                
                while left<=right and idle_count > 0 and counter[freq[0]] > 0:
                    if counter[freq[left]] > 0:
                        ans.append(freq[left])
                        counter[freq[left]] -= 1
                        idle_count -= 1
                        left += 1
                    elif counter[freq[right]] > 0:
                        ans.append(freq[right])
                        counter[freq[right]] -= 1
                        idle_count -= 1
                        right -= 1
                    else:
                        left += 1                     
                        
                while idle_count > 0 and counter[freq[0]] > 0:
                    ans.append('idle')
                    idle_count -= 1    

            if counter[freq[0]] == 0:
                freq.popleft()
            
            freq = deque(sorted(freq, key=lambda x:counter[x], reverse=True))
            print(ans)
        return len(ans)
        

# Tests
sol = Solution()
# Testcase 1; ["A","A","A","B","B","B"] n = 2 output = 8
# Testcase 2; ["A","A","A","B","B","B"] n = 3 output = 10
# Testcase 3; ["A","A","A","B","B","B", "C"] n = 3 output = 10
# Testcase 4; ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"] n = 2 output = 12
# Testcase 5; ["A","B","C","A"] n = 100 output = 102
# Testcase 6; ["C"] n = 3 output = 1
# Testcase 7; ["B","C","D","A","A","A","A","G"] n = 1 output = 8
# Testcase 8; [["A","B","C","D","A","B","V"] n = 3 output = 7
# ans = sol.leastInterval(["A","B","C","D","A","B","V"], 3)
# print(ans == 7)
ans = sol.leastInterval(["A", "A", "A", "C", "C", "B", "B", "B", "D"], 3)
print(ans == 10)
        