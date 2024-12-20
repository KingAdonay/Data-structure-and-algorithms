from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for num in range(1, n + 1):
            value = f"{num}"
            if num % 3 == 0 and num % 5 == 0:
                value = "FizzBuzz"
            elif num % 3 == 0:
                value = "Fizz"
            elif num % 5 == 0:
                value = "Buzz"
            
            answer.append(value)
        
        return answer
    

# Tests below
def checkSolution(actual, expected):
    status = 'passed'
    for index, value in enumerate(expected):
        if actual[index] != value:
            status = 'failed'
            break
    
    return status

solution = Solution()
# Testcase 1: n = 15
expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
answer = solution.fizzBuzz(15) 
print(checkSolution(answer, expected))

# Testcase 1: n = 5
expected = ["1","2","Fizz","4","Buzz"]
answer = solution.fizzBuzz(5) 
print(checkSolution(answer, expected))

# Testcase 1: n = 3
expected = ["1","2","Fizz"]
answer = solution.fizzBuzz(3) 
print(checkSolution(answer, expected))


