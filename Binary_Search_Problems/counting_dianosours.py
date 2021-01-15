"""
Counting Dinosaurs
You are given a string animals and another string dinosaurs. Every letter in animals represents a different type of animal and every unique character in dinosaurs represents a different dinosaur.

Return the total number of dinosaurs in animals.

Example 1
Input
animals = "abacabC"
dinosaurs = "bC"
Output
3
Explanation
There's two types of dinosaurs "b" and "C". There's 2 "b" dinosaurs and 1 "C" dinosaur. Note we didn't count the lowercase "c" animal as a dinosaur.

Example 2
Input
animals = "abc"
dinosaurs = "cd"
Output
1
Explanation
Only "c" is a match

Solved
1,609
Attempted
1,833
Rate
87.78%
"""
class Solution:
    def solve(self, animals, dinosaurs):
        count = 0
        for i in range(len(animals)):
           if animals[i] in dinosaurs:
               count += 1
        return count