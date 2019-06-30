#
# Author: Chanyut Yuvacharuskul
#
n = int(input())
c = list(map(int, input().split()))
def ads(t, x, i):
    for j in range(i, n):
        if j <= x+2:
            continue
        else:
            return max(ads(t, x, j+1), ads(t+c[j], j, j+1))
    return t
print(ads(0, float('-inf'), 0))
