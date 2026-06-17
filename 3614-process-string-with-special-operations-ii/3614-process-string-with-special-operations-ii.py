class Solution:
    def processStr(self, s: str, k: int) -> str:
        stack = []
        cur = 0
        for i in s:
            if i=="*":
                if cur:
                    cur-=1
            elif i=="#":
                cur*=2
            elif i=="%":
                pass
            else:
                cur+=1
            stack.append(cur)
        if k>=cur:
            return "."
        for j in range(len(s)-1,-1,-1):
            i=s[j]
            if i.isalpha():
                if k==stack[j]-1:
                    return i
            elif i=="#":
                half=stack[j]//2
                if k>=half:
                    k-=half
            elif i=="%":
                k=stack[j]-1-k
        return "."