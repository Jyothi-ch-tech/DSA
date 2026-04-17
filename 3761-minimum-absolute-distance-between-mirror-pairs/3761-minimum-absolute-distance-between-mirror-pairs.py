class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        
        d={}
        ans=float('inf')
        
        for i,num in enumerate(nums):
            if num in d:
                ans=min(ans,i-d[num])
            
            d[rev(num)]=i
        
        return ans if ans != float('inf') else -1