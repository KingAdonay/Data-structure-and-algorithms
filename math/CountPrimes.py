'''
    204. Count Primes
    
    To find the number of prime numbers less than the given number n, we can use the naive approach to find all prime numbers less than n
    by iterating through each number and checking if it is prime. However, this approach is inefficient for large values of n.
    A more efficient approach is to use the Sieve of Eratosthenes algorithm, which is a popular algorithm for finding all prime numbers up to a specified integer.
    The algorithm works by iteratively marking the multiples of a given prime number as composite if the number is higher that the square of the prime number.
    The steps of the Sieve of Eratosthenes algorithm are as follows:
    1. Create a boolean array is_prime of size n, initialized to True. The index of the array represents the number, and the value at that index indicates whether the number is prime or not.
    2. Mark the indices 0 and 1 as False, since 0 and 1 are not prime numbers.
    3. Iterate through the numbers starting from 2 up to the square root of n. For each number num:
       a. If is_prime[num] is True, it means num is a prime number. Mark all multiples of num starting from num^2 as False in the is_prime array.
    4. Finally, count the number of True values in the is_prime array, which will give us the count of prime numbers less than n.
    
    
    Time Complexity: O(n) due to the Sieve of Eratosthenes algorithm.
    Space Complexity: O(n) for the is_prime array.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True if i != 0 and i != 1 else False for i in range(n)]
        max_prime = int(pow(n, 1/2)) + 1
        for num in range(2, max_prime):
            if not is_prime[num]:
                continue
            
            sqr = num ** 2
            for i in range(sqr, n, num):
                is_prime[i] = False
        
        return is_prime.count(True)
            

# Testcases:
s = Solution()
print(s.countPrimes(10) == 4)
print(s.countPrimes(0) == 0)
print(s.countPrimes(1) == 0)
print(s.countPrimes(2) == 0)
print(s.countPrimes(3) == 1)
print(s.countPrimes(4) == 2)
print(s.countPrimes(1500000) == 114155)