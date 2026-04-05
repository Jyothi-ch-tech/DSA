class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        mod = 10**9 + 7
        length = 0
        
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                length += 1
            res = ((res << length) | i) % mod
        
        return res