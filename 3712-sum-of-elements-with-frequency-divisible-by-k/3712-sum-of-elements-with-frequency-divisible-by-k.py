class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans=0
        for i in d:
            if d[i]%k==0:
                ans+=(d[i]*i)
        return ans

        