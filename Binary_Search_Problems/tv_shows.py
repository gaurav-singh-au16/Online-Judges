"""
TV Shows
Given a list of strings shows, a list of integers durations, and an integer k, where shows[i] and durations[i] represent the name and duration watched by the ith person, return the total duration watched of the k most watched shows.

Example 1
Input
shows = ["Top Gun", "Aviator", "Top Gun", "Roma", "Logan"]
durations = [5, 3, 5, 13, 4]
k = 2
Output
23
Explanation
The top 2 most watched movies are "Roma" and "Top Gun" for total durations of 13 and 10 = 5+ 5.

Solved
486
Attempted
584
Rate
83.22%
"""

def solve(shows, durations, k):
    p1 = 0
    p2 = 0
    n_dict = {}
    while p1 < len(shows):
        if shows[p1] not in n_dict:
            n_dict[shows[p1]] = durations[p2]
            p1 += 1
            p2 += 1
        else:
            n_dict[shows[p1]] += durations[p2]
            p1 += 1
            p2 += 1
    ans = 0
    for i in range(k):
        Keymax = max(n_dict, key=n_dict.get)
        ans += n_dict[Keymax]
        del n_dict[Keymax]
    return ans
if __name__ == "__main__":
    shows = ["Top Gun", "Aviator", "Top Gun", "Roma", "Logan"]
    durations = [5, 3, 5, 13, 4]
    k = 2
    print(solve(shows, durations, k))