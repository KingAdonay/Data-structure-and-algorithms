import math
from typing import List

class Solution:
    def mergeValues(self, intervals, start, mid, end):
        n1 = mid - start + 1
        n2 = end - mid

        leftArr = []
        rightArr = []
        i = 0
        j = 0

        while i < n1:
            leftArr.append(intervals[start + i])
            i+=1
        while j < n2:
            rightArr.append(intervals[mid+ 1 + j])
            j += 1
        
        i = 0
        j = 0
        k = start

        while i < n1 and j < n2:
            if leftArr[i][0] <= rightArr[j][0]:
                intervals[k] = leftArr[i]
                i += 1
            else:
                intervals[k] = rightArr[j]
                j += 1

            k += 1
        
        while i < n1:
            intervals[k] = leftArr[i]
            i += 1
            k += 1

        while j < n2:
            intervals[k] = rightArr[j]
            j += 1
            k += 1

    def mergeSort(self, intervals: List[List[int]], start, end):
        if start >= end:
            return
        mid = math.floor(start + (end - start) / 2)
        self.mergeSort(intervals, start, mid)
        self.mergeSort(intervals, mid + 1, end)

        self.mergeValues(intervals, start, mid, end)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        self.mergeSort(intervals, 0, len(intervals) - 1)
        nonOverlappingIntervals = []

        i = 0
        j = 0
    
        intervalStart = intervals[0][0]
        intervalEnd = intervals[0][1]
        while i < len(intervals):
            if i == (len(intervals) - 1):
                nonOverlappingIntervals.append([intervalStart, intervalEnd])
                i+=1
                continue

            if intervals[i+1][0] <= intervalEnd:
                if intervals[i + 1][1] > intervalEnd:
                    intervalEnd = intervals[i+1][1]
            else:
                nonOverlappingIntervals.append([intervalStart, intervalEnd])
                intervalStart = intervals[i+1][0]
                intervalEnd = intervals[i+1][1]

            i += 1

        return nonOverlappingIntervals
        
    def checkValues(self, actualValue, expectedValue):
        for i, value in enumerate(actualValue):
            if (expectedValue[i] != value):
                print("Test failed.")
                return
        print("Test passed.")

# Tests
solution = Solution()

# Testcase 1: [[1,3],[2,6],[8,10],[15,18]]
expected = [[1,6],[8,10],[15,18]]
closestPoints = solution.merge([[1,3],[2,6],[8,10],[15,18]])
solution.checkValues(closestPoints, expected)

# Testcase 2: [[1,4],[2,3]]
expected = [[1,4]]
closestPoints = solution.merge([[1,4],[2,3]])
solution.checkValues(closestPoints, expected)