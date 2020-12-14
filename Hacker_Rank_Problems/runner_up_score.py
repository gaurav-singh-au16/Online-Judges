"""
Find the Runner-Up Score!
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    b = sorted(arr)
    a=b[::-1]
    for i in range(len(a)):
        if (a[0]==a[i+1]):
            continue
        else:
            print(a[i+1])
            break
