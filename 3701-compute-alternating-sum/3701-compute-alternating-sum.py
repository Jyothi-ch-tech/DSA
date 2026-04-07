class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ans=0
        for i in range(0,len(nums),2):
            ans+=nums[i]
        for i in range(1,len(nums),2):
            ans-=nums[i]
        return ans
        