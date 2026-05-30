class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in {"+","-","*","/"} :
                stack.append(int(i)) 
            else:
                a1=stack.pop()
                a2=stack.pop() 
                if i=="+":
                    stack.append(a1+a2)
                elif i=="-":
                    stack.append(a2-a1)
                elif i=="*":
                    stack.append(a1*a2)
                else:
                    stack.append(int(a2/a1))
        return stack[0]
