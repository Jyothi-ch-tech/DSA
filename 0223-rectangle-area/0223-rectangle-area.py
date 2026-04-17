class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1=abs(ax2-ax1)*abs(ay1-ay2)
        a2=abs(bx2-bx1)*abs(by1-by2)
        c1=max(0,min(ax2,bx2)-max(ax1,bx1))
        c2=max(0,min(ay2,by2)-max(ay1,by1))
        return a1+a2-c1*c2