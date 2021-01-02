"""
"""
def restoreString(s, indices):
    n_dict = {}
    p1 = 0
    ans = ""
    for i in range(len(indices)):
        n_dict[indices[i]] = s[p1]
        p1 += 1
    for value in range(len(n_dict)):
        ans += n_dict[value] 
    return ans
if __name__ == "__main__":
    s = "aiohn"
    indices = [3,1,4,2,0]
    print(restoreString(s, indices))
