class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP=nums[0]
        minP=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxP,minP=minP,maxP
            maxP=max(nums[i],maxP*nums[i])
            minP=min(nums[i],minP*nums[i])
            ans=max(ans,maxP)
        return ans
        

        