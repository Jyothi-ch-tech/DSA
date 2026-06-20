class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.extend([[1,0],[n,n-1]])
        restrictions.sort()
        m = len(restrictions)

        for i in range(1,m):
            restrictions[i][1] = min(restrictions[i][1],restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0])

        for i in range(m-2,-1,-1):
            restrictions[i][1] = min(restrictions[i][1],restrictions[i+1][1] + restrictions[i+1][0] - restrictions[i][0])

        max_val = 0

        for i in range(1,m):
            l,h1 = restrictions[i-1]
            r,h2 = restrictions[i]
            max_val = max(max_val,max(h1,h2) + (r-l-abs(h1-h2))//2)

        return max_val
        