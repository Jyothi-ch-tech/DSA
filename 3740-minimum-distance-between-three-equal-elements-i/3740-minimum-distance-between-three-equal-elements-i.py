class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')
        
        for i in range(n):
            count = 1
            
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    count += 1
                    if count == 3:
                        res = min(res, 2 * (j - i))
                        break
        
        return res if res != float('inf') else -1