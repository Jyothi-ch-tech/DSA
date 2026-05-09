class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = (-1 + (1+(8*n))**0.5)//2
        return int(x)
        
            

        