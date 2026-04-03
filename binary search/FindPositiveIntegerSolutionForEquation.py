from typing import List

'''
    1237. Find Positive Integer Solution for a Given Equation
    
    Use binary search to find all positive integer pairs (x, y) such that customfunction.f(x, y) == z.
    
    Intuition:
    - We can iterate through possible values of x from 1 to z, and for each
        x, we can use binary search to find the corresponding y value that satisfies the equation.  
    - If customfunction.f(x, mid) is less than z, it means we need to increase y, so we move the start pointer to mid + 1.
    - If customfunction.f(x, mid) is greater than z, it means we need
        to decrease y, so we move the end pointer to mid - 1.
    
    Time Complexity: O(z log(z)) since we iterate through possible values of x and for each x we perform a binary search on the range of possible y values.
    Space Complexity: O(1) since we only use a constant amount of extra space.
    
'''

def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        output = []
        for x in range(1, z + 1):
            # Binary Search for a correct y value
            start = 1
            end = z
            
            while start <= end:
                mid = start + (end - start) // 2
                
                # If we found a pair, add it to output array and break out of this inner loop
                if customfunction.f(x,mid) == z:
                    output.append([x,mid])
                    break
                
                # If we did not find a pair, try to move to left or right of mid
                # If the custom function returns a value less than z, we need to move to right of mid
                if customfunction.f(x,mid) < z: start = mid + 1
                # Otherwise to the left of mid
                else: end = mid - 1
                

        return output
    
# Testcases
# Testcase 1: customfunction = [[1,1,1],[1,2,2],[1,3,3],[2,1,2],[2,2,3],[2,3,4],[3,1,3],[3,2,4],[3,3,5]], z = 5 -> [[1,4],[2,3],[3,2]]