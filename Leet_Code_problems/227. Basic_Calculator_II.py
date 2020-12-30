"""
227. Basic Calculator II
Medium

1992

321

Add to List

Share
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
Accepted
237,165
Submissions
621,049
"""
class Solution:
    def calculate(self, s: str) -> int:
        
    
        if not s:
            return 0
        PRIORITY={
        "+":0,
        "-":0,
        "*":1,
        "/":1
        }   
        def operate(num1,num2,op)->int:
            if op=="+":
                return num1+num2
            if op=="-":
                return num1-num2
            if op == "*":
                return num1*num2
            if op == "/":
                return num1//num2

        num_stk=[]
        op_stk=[]
        op_set=set(["*","/","-","+"])
        dig_set=set([str(dig) for dig in range(0,10)])
        valid_char=set(op_set).union(set(dig_set))
        temp_num=""

        #fill stack
        for c in s:
            if c not in valid_char:
                continue
            if c in dig_set:
                temp_num=temp_num+c
                continue
            if c in op_set:
                num_stk.append(int(temp_num))
                temp_num=""
                while(len(op_stk) and PRIORITY[c]<=PRIORITY[op_stk[-1]]):
                    num2=num_stk.pop()
                    num1=num_stk.pop()
                    op=op_stk.pop()
                    num_stk.append(operate(num1,num2,op))
                op_stk.append(c)
        num_stk.append(int(temp_num))

        #empty out stack
        while(len(num_stk)!=1 and op_stk):
            num2=num_stk.pop()
            num1=num_stk.pop()
            op=op_stk.pop()
            num_stk.append(operate(num1,num2,op))

        return num_stk[-1]
    
    