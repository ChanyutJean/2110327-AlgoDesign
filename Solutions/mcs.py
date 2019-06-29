#
# Author: Chanyut Yuvacharuskul
#

l = int(input())
d = list(map(int, input().split()))
def m(d, r):
    if r == 0:
        return d[0]
    else:
        return max(d[r], m(d, r-1) + d[r])
x = float("-inf")
for i in range(l):
    a = m(d, i)
    if a > x:
        x = a
print(x)
