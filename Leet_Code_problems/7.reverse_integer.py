"""
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
"""

x = -123


#covert in list as string
l = []   
for i in str(x):
    l.append(i)
#reverse the list
a=l[::-1]
# remove the - from last and append to the first
for k in l:
    if k=="-": 
        a.pop(-1)
        a.insert(0,"-")
#Again Convert list into string
b=""
for j in a:
    b+=j
#Convert into integer    
c=int(b)

#Checking The Condition
if c >= 2**31-1 or c <= -(2**31) :
    print(0)
else:
    print(c)

    



