"""
"""
def solve(s):
    vow = ""
    cons = ""
    for ch in s:
        if ch in "aeiou":
            vow +=  ch
        else:
            cons += ch
    a = sorted(vow)
    b = sorted(cons)
    ans = "".join(a)+"".join(b)
    return ans
if __name__ == "__main__":
    s = "decalin"
    print(solve(s))