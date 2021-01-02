"""
1108. Defanging an IP Address
Easy

542

1019

Add to List

Share
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
"""
def defangIPaddr(address):
    n = len(address)
    p1 = 0
    ans = ""
    while p1 < n:
        if address[p1] == ".":
            ans += "[.]"
        else:
            ans += address[p1]
        p1 += 1
    return ans
if __name__ == "__main__":
    address = "1.1.1.1"
    print(defangIPaddr(address))
