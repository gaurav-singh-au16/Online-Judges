"""
155. Min Stack
Easy

4326

397

Add to List

Share
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.
Accepted
648,127
Submissions
1,414,224
"""
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.normal_stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        
        self.normal_stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            min_elem = min(x, self.min_stack[-1])
            self.min_stack.append(min_elem)
            

    def pop(self) -> None:
        self.normal_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.normal_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


