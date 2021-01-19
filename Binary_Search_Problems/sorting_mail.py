"""
Sorting Mail
You are given a list of mailboxes. Each mailbox is a list of strings, where each string is either "junk", "personal", "work". Go through each mailbox in round robin order starting from the first one, filtering out junk, to form a single pile and return the pile.

Example 1
Input
mailboxes = [
    ["work", "personal"],
    ["junk", "personal", "junk"],
    ["work"]
]
Output
["work", "work", "personal", "personal"]
Explanation
In order and without filtering, we'd have work -> junk -> work -> personal -> personal -> junk, and since we filter out junk we get work -> work -> personal -> personal.

Solved
350
Attempted
451
Rate
77.61%
"""
class Solution:
    def solve(self, mailboxes):
        if mailboxes == []:
            return []
        res = []
        n = max(len(i) for i in mailboxes) # find max length of aarry
        for i in range(n):
            for j in mailboxes:
                if i < len(j):
                    if j[i] != "junk":
                        res.append(j[i])
        return res