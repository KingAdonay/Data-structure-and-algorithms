import math
from typing import List

class Solution:
    def getDistance(self, point: List[int]):
        return math.sqrt((point[0]*point[0]) + (point[1] * point[1]))
    
    def merge(self, points: List[List[int]], left:int, mid:int, right: int):
        n1 = mid - left + 1
        n2 = right - mid

        leftArr = []
        rightArr = []

        i = 0
        j = 0
        while i < n1:
            leftArr.append(points[left + i])
            i += 1
        while j < n2:
            rightArr.append(points[mid + 1 + j])
            j += 1

        i = 0
        j = 0
        k = left
        while i < n1 and j < n2:
            if self.getDistance(leftArr[i]) <= self.getDistance(rightArr[j]):
                points[k] = leftArr[i]
                i += 1
            else:
                points[k] = rightArr[j]
                j += 1

            k += 1

        while i < n1:
            points[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < n2:
            points[k] = rightArr[j]
            j += 1
            k += 1
        

    def sortByDistance(self, points: List[List[int]], left: int, right: int):
        if left >= right:
            return
        mid = math.floor(left + (right - left) / 2)
        self.sortByDistance(points, left, mid)
        self.sortByDistance(points, mid+1, right)

        self.merge(points, left, mid, right)


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.sortByDistance(points, 0, len(points) - 1)

        return points[0:k]   
    
    def checkValues(self, actualValue, expectedValue):
        for i, value in enumerate(actualValue):
            if (expectedValue[i] != value):
                print("Test failed.")
                return
        print("Test passed.")

# Tests
solution = Solution()

# Testcase 1: [[3,3],[5,-1],[-2,4]], 2
expected = [[3,3],[-2,4]]
closestPoints = solution.kClosest([[3,3],[5,-1],[-2,4]], 2)
solution.checkValues(closestPoints, expected)

# Testcase2: [[1,3],[-2,2]], 1
expected = [[-2,2]]
closestPoints = solution.kClosest([[1,3],[-2,2]], 1)
solution.checkValues(closestPoints, expected)