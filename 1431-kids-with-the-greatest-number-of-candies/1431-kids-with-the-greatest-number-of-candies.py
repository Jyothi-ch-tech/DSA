class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxE=max(candies) 
        n=len(candies)
        temp=[False]*n
        for i in range(n):
            if candies[i]+extraCandies>=maxE:
                temp[i]=True 
        return temp

        
        