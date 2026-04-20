class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        lon=0
        for i in range(len(colors)-1):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    lon=max(lon,j-i)
        return lon
        