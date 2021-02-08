"""
"""
import math
 
 
def isPerfectSquare(x):
 
    #if x >= 0, 
    if(x >= 0):
        sr = math.sqrt(x)
         
        #return boolean T/F
        return ((sr*sr) == x)
    return False
 
# Driver code
 
 
x = 872
if (isPerfectSquare(x)):
    print("Yes")
else:
    print("No")