class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        s = 1 << nums[-1]
        for i in range(n):
            s += 1 << nums[i]
        return s - (1 << n) == (1 << (n+1)) - 2 
        