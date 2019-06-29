#
# Author: Chanyut Yuvacharuskul
#

def sim(a, b):
    if a == b:
        return True     
    if (len(a) == 1) or (len(b) == 1):
        return False
    a1, a2, b1, b2 = a[:int(len(a)/2)], a[int(len(a)/2):], b[:int(len(b)/2)], b[int(len(b)/2):]
    return True if (sim(a1, b1) and sim(a2, b2)) or (sim(a1, b2) and sim(a2, b1)) else False
print(sim(input(), input()))
    
