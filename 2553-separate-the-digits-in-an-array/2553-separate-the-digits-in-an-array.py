class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]: 
        temp=[]
        for i in range(len(nums)):
            for j in str(nums[i]):
                temp.append(int(j))
        return temp
        