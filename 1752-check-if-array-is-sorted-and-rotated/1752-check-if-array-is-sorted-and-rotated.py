class Solution:
    def check(self, nums: List[int]) -> bool:
        arr=[]
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                arr=nums[i:]+nums[:i]
        return sorted(nums)==arr if arr!=[] else True
        

        