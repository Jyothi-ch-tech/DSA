class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        f={}
        for num in nums:
            f[num]=f.get(num,0)+1 
        keys=sorted(f.keys())
        val=keys[0]
        for key in keys:
            if f[key]!=f[val]:
                return [val,key]
        return [-1,-1]
        