"""
Minimum Difference
Given two list of integers l0 and l1, return the smallest absolute difference between a number from the first list and a number from the second list.

Constraints

n ≤ 100,000 where n is the length of l0
m ≤ 100,000 where m is the length of l1
Example 1
Input
lst0 = [1, 6, 3]
lst1 = [15, 9, 10]
Output
3
Explanation
The smallest difference is 9 - 6.

Solved
308
Attempted
487
Rate
63.25%
"""
class Solution:
    def solve(self, lst0, lst1):
        m = len(lst0)
        n = len(lst1)
        lst0.sort() 
        lst1.sort() 
    
        a = 0
        b = 0
    
        # Initialize result as max value 
        result = sys.maxsize 
    
        # Scan Both Arrays upto 
        # sizeof of the Arrays 
        while (a < m and b < n): 
        
            if (abs(lst0[a] - lst1[b]) < result): 
                result = abs(lst0[a] - lst1[b]) 
    
            # Move Smaller Value 
            if (lst0[a] < lst1[b]): 
                a += 1
    
            else: 
                b += 1
        # return final sma result 
        return result