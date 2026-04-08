class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for row in grid:
            low=0 
            high=len(row)-1 
            ans=0
            while low<=high:
                mid=(low+high)//2 
                if row[mid]<0: 
                    ans=len(row)-mid
                    high=mid-1 
                else:
                    low=mid+1 
            count+=ans 
        return count



        