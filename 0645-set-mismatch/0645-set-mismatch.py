class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup=-1
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            if nums[idx]<0:
                dup=abs(nums[i])
            else:
                nums[idx] = -nums[idx] 
        miss=-1
        for i in range(len(nums)):
            if nums[i]>0:
                miss=i+1
        return [dup,miss]