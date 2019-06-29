#
# Author: Chanyut Yuvacharuskul
#
from math import floor
def num(a):
    while True:
        for i in range(len(a)):
            if a[i] not in [0, 1]:
                x = a.pop(i)
                a.insert(i, floor(x/2))
                a.insert(i+1, x%2)
                a.insert(i+2, floor(x/2))
                break
        else:
            break
    return a
n, l, r = map(int, input().split())
print(num([n])[l-1:r].count(1))
                     
