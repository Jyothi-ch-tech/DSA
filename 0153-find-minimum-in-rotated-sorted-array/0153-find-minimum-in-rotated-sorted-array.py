class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=nums[0]
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2 
            if nums[mid]>=ans:
                low=mid+1 
            else:
                ans=nums[mid]
                high=mid-1 
        return ans
            