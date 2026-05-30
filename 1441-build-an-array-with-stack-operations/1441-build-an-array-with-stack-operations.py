class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        stk=[] 
        temp=set(target)
        for i in range(1,n+1):
            if i in temp:
                stack.append("Push")
                stk.append(i)
            else:
                stack.append("Push")
                stack.append("Pop")
            if stk==target:
                break
        return stack


        