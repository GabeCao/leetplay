class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        k = -2
        ret = []
        while N:
            r = N % k
            N //= k
            if r < 0:
                r += -k
                N += 1
            ret.append(str(r))
        ret.reverse()
        return ''.join(ret)

# 方法二
def base2(self, x):
    res = []
    while x:
        res.append(x & 1)
        x = x >> 1
    return "".join(map(str, res[::-1] or [0]))

def baseNeg2(self, x):
    res = []
    while x:
        res.append(x & 1)
        x = -(x >> 1)
    return "".join(map(str, res[::-1] or [0]))