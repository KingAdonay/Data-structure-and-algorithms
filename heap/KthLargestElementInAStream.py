import heapq
from typing import List

'''
    703. Kth Largest Element in a Stream
    
    Intuition:
    To avoid sorting and adding new items into an array of length n, which will take O(n) for insetion, we can use a heap.
    Using a min-heap allow us to limit our space complexity to O(k), reduce the initialization time from O(nlogn) to O(nlogk), and add method would only 
    take O(logk) for each operation and constant time peek for the kth item which will be at the top of the heap since we are using a min heap.
    
    Approach:
    1. Define the add method which will take a single value, add it to the heap, validate the size of the heap to k, and return the kth value.
    2. Define a constructor that would take k and list of numbers to initialize the k property of the class and the heap.
    3. Use the add method to add each value in nums to the heap.
    
    Time complexity: O(nlogk) for initialization, and O(logk) for add
    Space complexity: O(k) for the heap
'''

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3,[4,5,8,2])
param_1 = obj.add(3)
print(param_1 == 4)
param_2 = obj.add(5)
print(param_2 == 5) 
