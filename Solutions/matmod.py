#
# Author: Chanyut Yuvacharuskul
#
n, k = map(int, input().split())
m = list(map(int, input().split()))
def mn(n, a, b, k):
    if n == 1:
        return a
    a1 = [i%k for i in a]
    b1 = [i%k for i in b]
    c1 = [a1[0]*b1[0] + a1[1]*b1[2],
          a1[0]*b1[1] + a1[1]*b1[3],
          a1[2]*b1[0] + a1[3]*b1[2],
          a1[2]*b1[1] + a1[3]*b1[3]]
    return mn(n-1, [i%k for i in c1], b, k)
print(mn(n, m, m, k))
