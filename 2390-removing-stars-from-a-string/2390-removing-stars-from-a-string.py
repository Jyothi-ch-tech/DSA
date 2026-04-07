class Solution:
    def removeStars(self, s: str) -> str:
        temp=[]
        for i in s:
            if temp and i == "*":
                temp.pop() 
            else:
                temp.append(i)
        return "".join(temp)
        