class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        f={}
        for num in nums:
            f[num]=f.get(num,0)+1
        for num in nums:
            if f[num]==1 and num%2==0:
                return num 
        return -1
        