class Solution:
    def mirrorDistance(self, n: int) -> int:
        def rev(num):
            res=0
            while num>0:
                res=res*10+num%10 
                num//=10 
            return res
        return abs(n-rev(n))