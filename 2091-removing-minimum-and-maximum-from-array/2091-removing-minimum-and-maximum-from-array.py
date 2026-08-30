class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        mini=min(nums)
        maxi=max(nums)
        ans=0
        maxi_idx=0
        mini_idx=0
        for i in range(len(nums)):
            if nums[i]==maxi:
                maxi_idx=i
            if nums[i]==mini:
                mini_idx=i 
        l=min(mini_idx, maxi_idx)
        r=max(mini_idx, maxi_idx)  
        ans=min(
            r+1,n-l,l+1+n-r
        )
        return ans 


            
        