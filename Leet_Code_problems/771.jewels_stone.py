"""
771. Jewels and Stones
Easy

2410

390

Add to List

Share
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
Accepted
578,220
Submissions
666,037
"""
def numJewelsInStones(jewels, stones):
    ans = 0
    for i in range(len(jewels)):
        for j in range(len(stones)):
            if jewels[i] == stones[j]:
                ans += 1
    return ans
if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    print(numJewelsInStones(jewels, stones))