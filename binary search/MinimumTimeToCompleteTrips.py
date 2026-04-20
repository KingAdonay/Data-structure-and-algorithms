from typing import List

'''
    2187. Minimum Time to Complete Trips
    
    We can use binary search to find the minimum time required to complete the given number of trips.
    We will define a helper function `get_num_of_trips` that calculates how many trips can be completed in a given time `t` based on the trip times provided in the `time` list.
    Then, we will perform a binary search on the range of possible times, starting from 1 to the maximum time it would take to complete all trips
    (which is the minimum trip time multiplied by the total number of trips).
    
    Time Complexity: O(n log m), where n is the number of trip times and m is the maximum time calculated. The binary search will take O(log m) and each call to `get_num_of_trips` will take O(n).
    Space Complexity: O(1) since we are using only a constant amount of extra space.
'''

class Solution:
    def get_num_of_trips(self, time: List[int], t: int) -> int:
        trips = 0
        for trip_time in time:
            trips += t // trip_time
        
        return trips
    
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        max_time = min(time) * totalTrips
        left, right = 1, max_time
        while left <= right:
            mid = (left + right) // 2
            if self.get_num_of_trips(time, mid) < totalTrips:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
    
# Testcases
# Testcase 1: time = [1,2,3], totalTrips = 5 -> 3
# Testcase 2: time = [2], totalTrips = 1 -> 2
# Testcase 3: time = [5,10,15], totalTrips = 10 -> 25